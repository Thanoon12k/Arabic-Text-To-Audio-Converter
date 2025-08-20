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
- Now includes six powerful media tools (PDFs, Office, Video, Images)

> Live Demo: Test it now at [texttomp3.pythonanywhere.com](https://texttomp3.pythonanywhere.com/)


## Features
- Text → MP3 in seconds using gTTS
- Arabic‑first UI (RTL) with Iraqi‑inspired styling
- One‑click playback in the browser and downloadable MP3
- No login required; privacy‑friendly
- Auto cleanup of generated files after ~1 hour (configurable)
- Robust error handling and MP3 duration validation (via Mutagen)
- Tools hub designed to scale to 30+ tools

### Included Tools
1) Images → PDF Converter
- Upload multiple images (JPEG/PNG)
- Reorder images manually
- Choose page size (A4/Letter)
- Output: single PDF that preserves image quality

2) PDF → Images Converter
- Convert selected pages or entire PDF
- Choose output quality (low/medium/high)
- Output: one image per page, packed as ZIP

3) PDF → Office Converter
- Convert PDF to DOCX, XLSX, or PPTX
- Extract text per page and/or render slides as images
- Output: editable Office files as close as possible to original

4) Office → MP3 Converter
- Upload DOCX/PPTX and convert the text to MP3
- Choose Arabic/English, set TLD (e.g., com.sa) and speed (normal/slow)
- Output: MP3 with inline streaming + download

5) Video → Audio Converter
- Extract audio track from videos (MP4/MKV/AVI…)
- Select format (MP3/WAV/OGG), bitrate, and time range
- Output: audio file ready to download

6) Image Background Remover
- AI‑based automatic background removal
- Download transparent PNG and quick preview
- Ideal for product photos and design workflows


## Installation Instructions

### Prerequisites
- Python 3.10+
- Internet connectivity (gTTS calls Google’s TTS)
- For video: FFmpeg installed on the system (moviepy depends on it)

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

### Text‑to‑MP3 (Arabic/English)
1. افتح الصفحة الرئيسية.
2. اختر اللغة (افتراضياً العربية).
3. أدخل النص (مثال: "مرحبا يا أعزائي كيف حالكم اليوم").
4. اضغط "حوّل إلى MP3".
5. استمع مباشرة أو قم بالتنزيل.

### Images → PDF
- الذهاب: `/tools/images-to-pdf`
- ارفع عدة صور، غيّر ترتيبها إن شئت، اختر حجم الصفحة، ثم اضغط "تحويل" للحصول على ملف PDF.

### PDF → Images
- الذهاب: `/tools/pdf-to-images`
- ارفع ملف PDF، اختر الصفحات (مثلاً 1-3,5) والجودة، ثم حمّل ملف ZIP للصور الناتجة.

### PDF → Office (DOCX/XLSX/PPTX)
- الذهاب: `/tools/pdf-to-office`
- ارفع PDF، اختر الهدف (وورد/إكسل/باوربوينت) والصفحات، حمّل الملف الناتج.

### Office → MP3
- الذهاب: `/tools/office-to-mp3`
- ارفع DOCX أو PPTX، اختر اللغة والسرعة وTLD، استمع للملف أو حمّله.

### Video → Audio
- الذهاب: `/tools/video-to-audio`
- ارفع فيديو، اختر الصيغة والجودة والمدى (اختياري)، ثم حمّل الصوت المستخرج.

### Image Background Remover
- الذهاب: `/tools/background-remover`
- ارفع صورة ثم احصل على نسخة بخلفية شفافة (PNG) مع معاينة فورية.


## Deployed Version
- Live: [texttomp3.pythonanywhere.com](https://texttomp3.pythonanywhere.com/) — جرّب الآن وشاركنا رأيك!


## Contributing
Contributions are welcome! Here’s how to get started:
1. Fork the repository
2. Create a feature branch: `git checkout -b feat/your-feature`
3. Commit changes: `git commit -m "feat: add your feature"`
4. Push to your fork: `git push origin feat/your-feature`
5. Open a Pull Request with a clear description and screenshots if UI changes

Ideas to explore:
- More tools under the `/tools` hub (goal: 30+ tools)
- Offline TTS fallback (e.g., pyttsx3)
- Voice selection UI, speed, and markers per paragraph
- Batch processing and queues


## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.


## Technologies Used
- ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) Python 3.10+
- ![Flask](https://img.shields.io/badge/-Flask-000000?logo=flask&logoColor=white) Flask (backend, routes, downloads/streaming)
- ![TailwindCSS](https://img.shields.io/badge/-Tailwind_CSS-06B6D4?logo=tailwindcss&logoColor=white) Tailwind CSS (UI styling, RTL layout)
- ![gTTS](https://img.shields.io/badge/-gTTS-34A853?logo=google&logoColor=white) Google Text‑to‑Speech (text → MP3)
- ![Mutagen](https://img.shields.io/badge/-Mutagen-FF6F00) Mutagen (MP3 duration validation)
- ![Pillow](https://img.shields.io/badge/-Pillow-3776AB?logo=python&logoColor=white) PIL/Pillow (image processing)
- ![PyMuPDF](https://img.shields.io/badge/-PyMuPDF-0096FF) PyMuPDF (PDF rendering & extraction)
- ![python-docx](https://img.shields.io/badge/-python--docx-1F6FEB) DOCX parsing
- ![python-pptx](https://img.shields.io/badge/-python--pptx-1F6FEB) PPTX parsing
- ![openpyxl](https://img.shields.io/badge/-openpyxl-1F6FEB) XLSX writing
- ![MoviePy](https://img.shields.io/badge/-MoviePy-FF0000?logo=ffmpeg&logoColor=white) MoviePy/FFmpeg (video→audio)
- ![rembg](https://img.shields.io/badge/-rembg-00A67E) AI background removal
- ![PythonAnywhere](https://img.shields.io/badge/-PythonAnywhere-1f2532?logo=python&logoColor=white) PythonAnywhere (deployment)


## Contact Information
Have questions, suggestions, or ideas for new tools?
- Open an Issue on GitHub
- Or email: engthanoon1@gmail.com

---

If you find this project useful, please ⭐ the repository, try the [live demo](https://texttomp3.pythonanywhere.com/), and consider contributing new tools to the `/tools` hub! 