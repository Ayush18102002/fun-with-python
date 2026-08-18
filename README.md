# 🐍 Fun with Python

A collection of Python mini-projects and utilities built to explore Python programming, automation, AI, multimedia processing, image manipulation, text-to-speech, and PDF utilities.

This repository contains practical scripts that demonstrate different Python libraries and real-world use cases.

## 📂 Repository Structure

```text
fun-with-python/
│
├── background_removal/
│   └── removal.py
│
├── calendar/
│   └── calendar.py
│
├── chatbot-gemini/
│   └── main.py
│
├── pdf_protector/
│   └── protect.py
│
├── text-to-speech/
│   ├── google-gtts.py
│   └── microsoft-edge-tts.py
│
├── video-to-gif/
│   └── mediapy.py
│
├── video_to_text/
│   └── main.py
│
├── venv/
│
├── .gitignore
├── LICENSE
└── README.md
```

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

The program prints the calendar for the selected month.

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
geminie-chatbot/main.py
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
* Extracts the audio from the video.
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

Convert text into natural-sounding speech using two different approaches.

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

---

### 🎥 Video to GIF Converter

Convert videos into animated GIFs using Python.

**Features**

* Reads video files.
* Converts video frames into GIF format.
* Built using the `mediapy` library.
* Useful for creating short animations and demonstrations.

---

### 🖼️ Background Removal

Remove backgrounds from images automatically using AI.

**Features**

* Automatically removes image backgrounds.
* Uses `rembg` for AI-powered background removal.
* Uses `PIL (Pillow)` for image processing.
* Supports transparent-background images.
* Useful for profile pictures, product images, graphics, and other image-processing tasks.

**Libraries**

* `rembg`
* `Pillow`

**Main script**

```text
background_removal/removal.py
```

---

### 🔐 PDF Protector

Encrypt PDF files with a password to help protect them from unauthorized access.

**Features**

* Takes a PDF file as input.
* Allows the user to set a password.
* Encrypts PDFs using the `pypdf` library.
* Creates password-protected PDF files.

**Library**

* `pypdf`

**Main script**

```text
pdf_protector/protect.py
```

---

## 🛠️ Technologies Used

* **Python** — Main programming language.
* **Google Gen AI** — Gemini API integration.
* **Whisper** — Speech-to-text transcription.
* **gTTS** — Google Text-to-Speech.
* **Edge TTS** — Microsoft Edge Text-to-Speech.
* **MediaPy** — Video and media processing.
* **rembg** — AI-powered image background removal.
* **Pillow** — Image processing.
* **pypdf** — PDF processing and encryption.
* **Calendar** — Python's built-in calendar module.

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Ayush18102002/fun-with-python.git
```

Move into the project directory:

```bash
cd fun-with-python
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

On Windows:

```powershell
venv\Scripts\activate
```

Install the required packages:

```bash
pip install gTTS edge-tts mediapy rembg pillow pypdf google-genai openai-whisper
```

> The Calendar Generator uses Python's built-in `calendar` module, so no additional package is required.

### FFmpeg

The **Video to Text** project uses Whisper and requires FFmpeg for processing video and audio files.

After installing FFmpeg, verify that it is available from your terminal:

```bash
ffmpeg -version
```

## ▶️ Running the Projects

### 📅 Calendar Generator

```bash
python calendar/calendar.py
```

### 🤖 Gemini Chatbot

```bash
python geminie-chatbot/main.py
```

Make sure your Gemini API key is configured before running the chatbot.

### 🎙️ Video to Text

```bash
python video_to_text/main.py
```

Place your video file in the appropriate project directory or provide the correct path to the video in `main.py`.

### 🔊 Google Text-to-Speech

```bash
python text-to-speech/google-gtts.py
```

### 🔊 Microsoft Edge TTS

```bash
python text-to-speech/microsoft-edge-tts.py
```

### 🎥 Video to GIF

```bash
python video-to-gif/mediapy.py
```

### 🖼️ Background Removal

```bash
python background_removal/removal.py
```

### 🔐 PDF Protector

```bash
python pdf_protector/protect.py
```

## 🎯 Purpose

This repository is a collection of Python practice projects designed to:

* Learn and improve Python programming.
* Explore useful third-party libraries.
* Experiment with AI and generative AI.
* Build small but practical applications.
* Work with images, audio, video, and PDF files.
* Explore speech-to-text and text-to-speech technologies.
* Practice automation and multimedia processing.
* Improve problem-solving and programming skills.
* Experiment with different Python libraries and real-world use cases.

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository, make your changes, and submit a pull request.

## ⭐ Support

If you found this repository helpful, consider giving it a **⭐ Star** on GitHub.

Happy Coding! 🚀
