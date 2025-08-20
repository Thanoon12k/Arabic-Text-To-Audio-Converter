# Arabic Text‑To‑Audio Converter (Flask + Tailwind)

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Backend-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-Frontend-06B6D4?logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)
[![gTTS](https://img.shields.io/badge/gTTS-Text--to--Speech-34A853?logo=google&logoColor=white)](https://pypi.org/project/gTTS/)
[![Mutagen](https://img.shields.io/badge/Mutagen-MP3%20Metadata-FF6F00)](https://mutagen.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)


## Project Overview
Arabic Text‑To‑Audio Converter is a modern, login‑free web app that converts Arabic (and English) text into high‑quality MP3 audio. It’s designed for speed, simplicity, and a great mobile experience, with an Arabic, right‑to‑left UI inspired by Mesopotamian aesthetics.

- Built with a production‑ready Flask backend and a Tailwind CSS frontend
- Supports inline audio playback (streaming) and file downloads
- Validates generated files to avoid “silent” or zero‑second MP3s

> Live Demo: Test it now at [texttomp3.pythonanywhere.com](https://texttomp3.pythonanywhere.com/)


## Features
- Text → MP3 in seconds using gTTS
- Arabic‑first UI (RTL) with Iraqi‑inspired styling
- One‑click playback in the browser and downloadable MP3
- No login required; privacy‑friendly
- Auto cleanup of generated files after ~1 hour (configurable)
- Robust error handling and MP3 duration validation (via Mutagen)
- Ready for expansion with a dedicated tools hub to host 30+ future tools


## Installation Instructions

### Prerequisites
- Python 3.10+
- Internet connectivity (gTTS calls Google’s TTS service)

### 1) Clone the repository
```bash
git clone <your-fork-or-repo-url>
cd <repo-folder>
```

### 2) Create and activate a virtual environment
- Windows (PowerShell):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```
- macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3) Install dependencies
```bash
pip install -r requirements.txt
```

### 4) Run the app (local dev)
```bash
python app.py
```
Open `http://127.0.0.1:5000` in your browser.

### Optional Environment Variables
- `GTTS_TLD` – choose TLD for Arabic regional voice (e.g., `com`, `com.sa`, `com.eg`). Default: `com`
- `MAX_TEXT_LENGTH` – limit input size. Default: `5000`
- `CLEANUP_MAX_AGE_SECONDS` – auto‑delete audio after N seconds. Default: `3600`
- `MIN_DURATION_SECONDS` – minimal acceptable MP3 duration. Default: `0.3`

Examples:
- Windows (PowerShell):
```powershell
$env:GTTS_TLD='com.sa'; python app.py
```
- macOS/Linux:
```bash
export GTTS_TLD=com.sa
python app.py
```

### Deployment (PythonAnywhere)
1. Upload project to PythonAnywhere (e.g., `~/text-to-mp3/`).
2. Create a virtualenv and install requirements:
```bash
mkvirtualenv --python=/usr/bin/python3.10 ttsenv
workon ttsenv
pip install -r /home/<username>/text-to-mp3/requirements.txt
```
3. Create a “Manual configuration” Flask app in the Web tab.
4. Point the WSGI file to your project and ensure it imports `application` from `wsgi.py`.
5. Reload the web app. Configure environment variables in the Web tab if desired.


## Usage Instructions

### From the Web UI
1. Open the app.
2. Select language (default Arabic).
3. Paste or type your text (e.g., "مرحبا يا أعزائي كيف حالكم اليوم").
4. Click “حوّل إلى MP3”.
5. Press play to stream inline or click “تنزيل MP3” to save the file.

### From the API
- Convert (JSON):
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"text":"مرحباً بكم جميعاً","lang":"ar"}' \
  http://127.0.0.1:5000/api/convert
```
Response:
```json
{
  "success": true,
  "filename": "tts_<id>.mp3",
  "url": "/download/tts_<id>.mp3",
  "stream_url": "/stream/tts_<id>.mp3"
}
```
- Stream inline:
```
GET /stream/tts_<id>.mp3
```
- Download as attachment:
```
GET /download/tts_<id>.mp3
```


## Deployed Version
- Live: [texttomp3.pythonanywhere.com](https://texttomp3.pythonanywhere.com/) — Try it now and share your feedback!


## Contributing
Contributions are welcome! Here’s how to get started:
1. Fork the repository
2. Create a feature branch: `git checkout -b feat/your-feature`
3. Commit changes: `git commit -m "feat: add your feature"`
4. Push to your fork: `git push origin feat/your-feature`
5. Open a Pull Request with a clear description and screenshots if UI changes

Ideas to explore:
- New tools under the `/tools` hub (goal: 30+ tools) — text utilities, format converters, AI helpers
- Offline TTS fallback (e.g., pyttsx3)
- Voice selection, speed, and pitch controls
- Multi‑language UI


## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.


## Technologies Used
- ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) Python 3.10+
- ![Flask](https://img.shields.io/badge/-Flask-000000?logo=flask&logoColor=white) Flask (backend, routes, downloads/streaming)
- ![TailwindCSS](https://img.shields.io/badge/-Tailwind_CSS-06B6D4?logo=tailwindcss&logoColor=white) Tailwind CSS (UI styling, RTL layout)
- ![gTTS](https://img.shields.io/badge/-gTTS-34A853?logo=google&logoColor=white) Google Text‑to‑Speech (text → MP3)
- ![Mutagen](https://img.shields.io/badge/-Mutagen-FF6F00) Mutagen (MP3 duration validation)
- ![PythonAnywhere](https://img.shields.io/badge/-PythonAnywhere-1f2532?logo=python&logoColor=white) PythonAnywhere (deployment)


## Contact Information
Have questions, suggestions, or ideas for new tools?
- Open an Issue on GitHub
- Or email: engthanoon1@gmail.com


---

If you find this project useful, please ⭐ the repository, try the [live demo](https://texttomp3.pythonanywhere.com/), and consider contributing new tools to the `/tools` hub! 