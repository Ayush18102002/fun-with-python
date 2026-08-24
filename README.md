Absolutely. I’d update the README to include the new `youtube_video_download/` project, its `main.py`, the `yt-dlp` dependency, and the **FFmpeg requirement** because `yt-dlp` may need FFmpeg to merge separate video/audio streams.

I also aligned the repository structure with what is currently visible in your VS Code Explorer.

# 🐍 Fun with Python

A collection of Python mini-projects and utilities built to explore Python programming, automation, AI, multimedia processing, image manipulation, text-to-speech, PDF utilities, and video downloading.

This repository contains practical Python scripts that demonstrate different libraries and real-world use cases.

---

## 📂 Repository Structure

```text
fun-with-python/

│
├── background_removal/
│   └── removal.py
│
├── calender/
│   └── calender.py
│
├── chatbot-gemini/
│   └── main.py
│
├── pdf_protector/
│   └── protect.py
│
├── text-to-speech/
│   ├── edge-tts-microsoft.py
│   └── text-to-voice.py
│
├── video_to_text/
│   └── main.py
│
├── video-to-gif/
│   └── video-to-gif.py
│
├── youtube_video_download/
│   └── main.py
│
├── venv/
│
├── .gitignore
├── LICENSE
├── README.md
└── pyvenv.cfg
```

---

## 🚀 Projects

### 📅 Calendar Generator

Generate a calendar for any month and year directly from the terminal.

**Features**

* Accepts user input for month and year.
* Displays a formatted monthly calendar.
* Built using Python's built-in `calendar` module.

**Example**

```text
Enter Year: 2026
Enter Month: 8
```

The program prints the formatted calendar for the selected month.

---

### 🤖 Gemini Chatbot

A simple command-line AI chatbot built using Google's Gemini API and the Google Gen AI Python SDK.

The project uses:

```python
from google import genai
```

**Features**

* Interactive command-line chatbot.
* Sends user questions to Gemini.
* Displays Gemini's responses in the terminal.
* Demonstrates how to integrate a generative AI API with Python.

**Main script**

```text
chatbot-gemini/main.py
```

**Library**

* `google-genai`

> **Note:** An API key is required to use the Gemini API.

---

### 🎙️ Video to Text

Convert the speech from a video into text using OpenAI Whisper.

The project uses:

```python
import whisper
```

**Features**

* Accepts video files as input.
* Extracts audio from the video.
* Transcribes spoken content into text.
* Uses the Whisper speech-recognition model.

**Main script**

```text
video_to_text/main.py
```

**Library**

* `openai-whisper`

> **Note:** Whisper requires FFmpeg to process video and audio files.

---

### 🔊 Text-to-Speech

Convert text into natural-sounding speech using different text-to-speech approaches.

#### 1. Google gTTS

Uses the Google Text-to-Speech library to convert text into an MP3 audio file.

**Features**

* Simple text-to-speech conversion.
* Generates MP3 audio files.
* Easy to use with Python.

#### 2. Microsoft Edge TTS

Uses Microsoft's Edge Text-to-Speech voices to generate high-quality speech.

**Features**

* Natural-sounding voices.
* Multiple languages and voices.
* Supports different voice options.

**Project files**

```text
text-to-speech/
├── edge-tts-microsoft.py
└── text-to-voice.py
```

**Libraries**

* `gTTS`
* `edge-tts`

---

### 🎥 Video to GIF Converter

Convert videos into animated GIF files using Python.

**Features**

* Reads video files.
* Converts video frames into GIF format.
* Uses the `mediapy` library.
* Useful for creating short animations and demonstrations.

**Main script**

```text
video-to-gif/video-to-gif.py
```

**Library**

* `mediapy`

---

### 🖼️ Background Removal

Remove backgrounds from images automatically using AI.

**Features**

* Automatically removes image backgrounds.
* Uses `rembg` for AI-powered background removal.
* Uses `Pillow` for image processing.
* Supports transparent-background images.
* Useful for profile pictures, product images, graphics, and other image-processing tasks.

**Main script**

```text
background_removal/removal.py
```

**Libraries**

* `rembg`
* `Pillow`

---

### 🔐 PDF Protector

Encrypt PDF files with a password to help protect them from unauthorized access.

**Features**

* Takes a PDF file as input.
* Allows the user to set a password.
* Encrypts PDFs using the `pypdf` library.
* Creates password-protected PDF files.

**Main script**

```text
pdf_protector/protect.py
```

**Library**

* `pypdf`

---

### 📥 YouTube Video Downloader

Download YouTube videos using Python and the `yt-dlp` library.

The project uses:

```python
import yt_dlp
```

**Features**

* Accepts a YouTube URL from the user.
* Downloads YouTube videos using `yt-dlp`.
* Supports video and audio formats available through `yt-dlp`.
* Uses FFmpeg to merge separate video and audio streams when required.

**Main script**

```text
youtube_video_download/main.py
```

**Library**

* `yt-dlp`

Install the Python package with:

```bash
pip install yt-dlp
```

> **Note:** FFmpeg is also required when `yt-dlp` needs to merge separate video and audio formats.

---

## 🛠️ Technologies Used

* **Python** — Main programming language.
* **Google Gen AI** — Gemini API integration.
* **yt-dlp** — YouTube video downloading.
* **Whisper** — Speech-to-text transcription.
* **gTTS** — Google Text-to-Speech.
* **Edge TTS** — Microsoft Edge Text-to-Speech.
* **MediaPy** — Video and media processing.
* **rembg** — AI-powered image background removal.
* **Pillow** — Image processing.
* **pypdf** — PDF processing and encryption.
* **Calendar** — Python's built-in calendar module.

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Ayush18102002/fun-with-python.git
```

Move into the project directory:

```bash
cd fun-with-python
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

On Windows:

```powershell
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install Python Dependencies

Install the required packages:

```bash
pip install gTTS edge-tts mediapy rembg pillow pypdf google-genai openai-whisper yt-dlp
```

The Calendar Generator uses Python's built-in `calendar` module, so no additional package is required.

---

## ⚙️ FFmpeg

Some projects in this repository require **FFmpeg**.

FFmpeg is required by:

* **Video to Text** — Whisper uses FFmpeg to process video and audio.
* **YouTube Video Downloader** — `yt-dlp` can use FFmpeg to merge separate video and audio streams.

After installing FFmpeg, verify that it is available from your terminal:

```bash
ffmpeg -version
```

If the command displays the FFmpeg version, it is installed correctly.

> **Windows:** FFmpeg must be added to your system `PATH` so that Python libraries and `yt-dlp` can find it.

---

## ▶️ Running the Projects

### 📅 Calendar Generator

```bash
python calender/calender.py
```

---

### 🤖 Gemini Chatbot

```bash
python chatbot-gemini/main.py
```

Make sure your Gemini API key is configured before running the chatbot.

---

### 🎙️ Video to Text

```bash
python video_to_text/main.py
```

Place your video file in the appropriate project directory or provide the correct path to the video in `main.py`.

---

### 🔊 Google Text-to-Speech

```bash
python text-to-speech/text-to-voice.py
```

---

### 🔊 Microsoft Edge TTS

```bash
python text-to-speech/edge-tts-microsoft.py
```

---

### 🎥 Video to GIF

```bash
python video-to-gif/video-to-gif.py
```

---

### 🖼️ Background Removal

```bash
python background_removal/removal.py
```

---

### 🔐 PDF Protector

```bash
python pdf_protector/protect.py
```

---

### 📥 YouTube Video Downloader

```bash
python youtube_video_download/main.py
```

The program will ask you for a YouTube URL:

```text
Youtube URL : Your Youtube Video Url
```

The video will then be downloaded using `yt-dlp`.

---

## 🎯 Purpose

This repository is a collection of Python practice projects designed to:

* Learn and improve Python programming.
* Explore useful third-party libraries.
* Experiment with AI and generative AI.
* Build small but practical applications.
* Work with images, audio, video, and PDF files.
* Explore speech-to-text and text-to-speech technologies.
* Practice automation and multimedia processing.
* Download online videos using Python.
* Improve problem-solving and programming skills.
* Experiment with different Python libraries and real-world use cases.

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository, make your changes, and submit a pull request.

---

## ⭐ Support

If you found this repository helpful, consider giving it a **⭐ Star** on GitHub.

Happy Coding! 🚀
