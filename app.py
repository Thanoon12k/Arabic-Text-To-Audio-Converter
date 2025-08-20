import os
import time
import uuid
from flask import Flask, request, jsonify, render_template, send_from_directory, url_for, abort
from gtts import gTTS

# Flask application setup
app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
AUDIO_DIR = os.path.join(BASE_DIR, 'generated')
os.makedirs(AUDIO_DIR, exist_ok=True)

# Configuration
MAX_TEXT_LENGTH = int(os.environ.get('MAX_TEXT_LENGTH', 5000))
CLEANUP_MAX_AGE_SECONDS = int(os.environ.get('CLEANUP_MAX_AGE_SECONDS', 3600))  # 1 hour by default


def clean_old_files() -> None:
	"""Delete generated MP3 files older than CLEANUP_MAX_AGE_SECONDS."""
	try:
		now = time.time()
		for entry in os.scandir(AUDIO_DIR):
			if not entry.is_file():
				continue
			if not entry.name.lower().endswith('.mp3'):
				continue
			try:
				mtime = entry.stat().st_mtime
				if now - mtime > CLEANUP_MAX_AGE_SECONDS:
					os.remove(entry.path)
			except FileNotFoundError:
				# If the file disappeared between scandir and stat/remove
				continue
	except Exception:
		# Do not let cleanup errors crash requests
		pass


def generate_unique_filename() -> str:
	return f"tts_{uuid.uuid4().hex}.mp3"


@app.get('/')
def index():
	clean_old_files()
	return render_template('index.html')


@app.post('/api/convert')
def convert_text_to_mp3():
	clean_old_files()
	# Support JSON or form-encoded
	text = ''
	lang = 'en'
	if request.is_json:
		payload = request.get_json(silent=True) or {}
		text = (payload.get('text') or '').strip()
		lang = (payload.get('lang') or 'en').strip() or 'en'
	else:
		text = (request.form.get('text') or '').strip()
		lang = (request.form.get('lang') or 'en').strip() or 'en'

	if not text:
		return jsonify({
			'success': False,
			'error': 'Text is required.'
		}), 400

	if len(text) > MAX_TEXT_LENGTH:
		return jsonify({
			'success': False,
			'error': f'Text exceeds maximum length of {MAX_TEXT_LENGTH} characters.'
		}), 413

	filename = generate_unique_filename()
	file_path = os.path.join(AUDIO_DIR, filename)

	try:
		tts = gTTS(text=text, lang=lang)
		tts.save(file_path)
	except Exception as exc:
		# Clean up partial file if created
		try:
			if os.path.exists(file_path):
				os.remove(file_path)
		except Exception:
			pass
		return jsonify({
			'success': False,
			'error': f'Failed to generate audio: {str(exc)}'
		}), 500

	download_url = url_for('download_file', filename=filename, _external=True)
	stream_url = url_for('stream_file', filename=filename, _external=True)
	return jsonify({
		'success': True,
		'filename': filename,
		'url': download_url,
		'stream_url': stream_url
	})


@app.get('/download/<path:filename>')
def download_file(filename: str):
	# Basic security checks
	basename = os.path.basename(filename)
	if basename != filename:
		abort(400)
	if not basename.lower().endswith('.mp3'):
		abort(400)

	file_path = os.path.join(AUDIO_DIR, basename)
	if not os.path.isfile(file_path):
		abort(404)

	# Use Flask 2.0+ download_name argument
	return send_from_directory(
		AUDIO_DIR,
		basename,
		as_attachment=True,
		download_name=basename,
		mimetype='audio/mpeg'
	)


@app.get('/stream/<path:filename>')
def stream_file(filename: str):
	# Basic security checks
	basename = os.path.basename(filename)
	if basename != filename:
		abort(400)
	if not basename.lower().endswith('.mp3'):
		abort(400)

	file_path = os.path.join(AUDIO_DIR, basename)
	if not os.path.isfile(file_path):
		abort(404)

	return send_from_directory(
		AUDIO_DIR,
		basename,
		as_attachment=False,
		mimetype='audio/mpeg'
	)


@app.errorhandler(404)
def not_found(_):
	return jsonify({'success': False, 'error': 'Not found'}), 404


@app.errorhandler(500)
def internal_error(_):
	return jsonify({'success': False, 'error': 'Internal server error'}), 500


if __name__ == '__main__':
	# For local development only; PythonAnywhere will use WSGI
	app.run(host='0.0.0.0', port=5000, debug=True) 