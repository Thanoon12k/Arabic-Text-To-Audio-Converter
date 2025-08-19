# Text to MP3 (Flask + Tailwind)

A simple, login-free web app that converts input text to an MP3 file using gTTS.

## Features
- Text → MP3 using Google Text-to-Speech (gTTS)
- No login or authentication
- Downloadable MP3 after conversion
- Auto-cleanup of generated files (by default after ~1 hour)
- Tailwind CSS (via CDN) responsive UI

## Quick Start (Local)

1. Create and activate a virtual environment (recommended):
```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# Windows cmd
.\.venv\Scripts\activate.bat
# Unix/macOS
source .venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
python app.py
```

4. Open the app at `http://127.0.0.1:5000`.

## Environment Variables (optional)
- `MAX_TEXT_LENGTH`: Maximum input characters (default: 5000)
- `CLEANUP_MAX_AGE_SECONDS`: Age in seconds after which MP3 files are deleted (default: 3600)

## Deployment on PythonAnywhere

1. Upload the project files to your PythonAnywhere account (e.g., into `~/TextToMp3`).
2. Create a virtualenv on PythonAnywhere (recommended Python 3.x):
```bash
mkvirtualenv --python=/usr/bin/python3.10 ttsenv
workon ttsenv
pip install -r /home/<your-username>/TextToMp3/requirements.txt
```
3. On the PythonAnywhere dashboard, go to Web → Add a new web app → Manual configuration (Flask).
4. Set the working directory to your project folder and set the WSGI file to import `application` from `wsgi.py` (the provided `wsgi.py` already exposes `application`).
5. Reload the web app. Visit your PythonAnywhere domain to use the converter.

Notes:
- PythonAnywhere will run your app behind its production WSGI server. Do not use `app.run()` there; the provided `wsgi.py` is used instead.
- The app serves generated MP3s via the `/download/<filename>` endpoint with correct `audio/mpeg` MIME type.
- Generated files are stored in the `generated/` directory and cleaned periodically on new requests.

## Tailwind CSS
The app uses Tailwind via the official CDN for simplicity. For larger apps, consider a build step (PostCSS) to tree-shake styles.

## Security Considerations
- Basic filename validation is performed on downloads.
- Input length is limited and errors are handled gracefully.

## License
MIT 