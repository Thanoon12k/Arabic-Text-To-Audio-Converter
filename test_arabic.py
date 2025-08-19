import json
import os
from mutagen.mp3 import MP3
from app import app, AUDIO_DIR


def main() -> None:
	client = app.test_client()

	arabic_text = "مرحباً! هذا اختبار لتحويل النص العربي إلى ملف صوتي إم بي ثري."
	resp = client.post(
		"/api/convert",
		data=json.dumps({"text": arabic_text, "lang": "ar"}),
		headers={"Content-Type": "application/json"},
	)
	print("/api/convert status:", resp.status_code)
	print("response:", resp.json)
	if resp.status_code != 200 or not resp.json or not resp.json.get("success"):
		raise SystemExit(1)

	filename = resp.json["filename"]
	file_path = os.path.join(AUDIO_DIR, filename)
	print("generated file:", file_path)
	if not os.path.isfile(file_path):
		raise RuntimeError("File not found after conversion")
	if os.path.getsize(file_path) <= 0:
		raise RuntimeError("Generated file is empty")

	# Duration validation
	audio = MP3(file_path)
	duration = float(getattr(audio.info, 'length', 0.0) or 0.0)
	print("duration:", duration)
	if duration <= 0.0:
		raise RuntimeError("Generated file has zero duration")

	# Test download route
	dl = client.get(f"/download/{filename}")
	print("/download status:", dl.status_code)
	print("content-type:", dl.headers.get("Content-Type"))
	if dl.status_code != 200:
		raise SystemExit(2)
	if "audio/mpeg" not in (dl.headers.get("Content-Type") or ""):
		raise RuntimeError("Unexpected MIME type for download")
	cd = dl.headers.get("Content-Disposition") or ""
	if "attachment" not in cd.lower():
		raise RuntimeError("Download should be an attachment")

	# Test stream route
	st = client.get(f"/stream/{filename}")
	print("/stream status:", st.status_code)
	print("stream content-type:", st.headers.get("Content-Type"))
	if st.status_code != 200:
		raise SystemExit(3)
	if "audio/mpeg" not in (st.headers.get("Content-Type") or ""):
		raise RuntimeError("Unexpected MIME type for stream")
	cds = (st.headers.get("Content-Disposition") or "").lower()
	if "attachment" in cds:
		raise RuntimeError("Stream should not be an attachment")


if __name__ == "__main__":
	main() 