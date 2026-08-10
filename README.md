# 🐍 Fun with Python

A collection of Python mini-projects and utilities built to explore Python programming, automation, multimedia processing, image manipulation, and PDF utilities. This repository contains practical scripts that demonstrate different Python libraries and real-world use cases.

## 📂 Repository Structure

```text
fun-with-python/
│
├── calendar/
│   └── calendar.py
│
├── text-to-speech/
│   ├── google-gtts.py
│   └── microsoft-edge-tts.py
│
├── video-to-gif/
│   └── mediapy.py
│
├── background_removal/
│   └── removal.py
│
├── pdf_protector/
│   └── protect.py
│
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

### 🔊 Text-to-Speech

Convert text into natural-sounding speech using two different approaches.

#### 1. Google gTTS

* Uses the Google Text-to-Speech (gTTS) library.
* Converts text into an MP3 audio file.
* Simple and easy to use.

#### 2. Microsoft Edge TTS

* Uses Microsoft's Edge Text-to-Speech voices.
* Produces high-quality, natural-sounding speech.
* Supports multiple languages and voice options.

---

### 🎥 Video to GIF Converter

Convert videos into animated GIFs using Python.

**Features**

* Reads video files.
* Converts video frames into GIF format.
* Built using the `mediapy` library.
* Useful for creating short animations or demonstrations.

---

### 🖼️ Background Removal

Remove the background from images automatically using Python.

**Features**

* Removes image backgrounds automatically.
* Uses the `rembg` library for AI-powered background removal.
* Uses `PIL (Pillow)` for image processing.
* Can generate images with transparent backgrounds.
* Useful for profile pictures, product images, graphics, and other image-processing tasks.

**Libraries Used**

* `rembg`
* `Pillow`

The main script is located at:

```text
background_removal/removal.py
```

---

### 🔐 PDF Protector

Encrypt PDF files with a password to help protect them from unauthorized access.

**Features**

* Takes a PDF file as input.
* Allows the user to set a password.
* Encrypts the PDF using the `pypdf` library.
* Creates a protected PDF file.
* Useful for securing personal or sensitive documents.

**Library Used**

* `pypdf`

The main script is located at:

```text
pdf_protector/protect.py
```

---

## 🛠️ Technologies Used

* **Python**
* **Calendar Module**
* **gTTS** – Google Text-to-Speech
* **Edge TTS** – Microsoft Edge Text-to-Speech
* **MediaPy** – Video and media processing
* **rembg** – AI-powered image background removal
* **Pillow (PIL)** – Image processing
* **pypdf** – PDF processing and encryption

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Ayush18102002/fun-with-python.git
```

Move into the project directory:

```bash
cd fun-with-python
```

Install the required Python packages:

```bash
pip install gTTS edge-tts mediapy rembg pillow pypdf
```

> The Calendar Generator uses Python's built-in `calendar` module, so no additional package is required for it.

## ▶️ Running the Projects

Run any project using Python.

### 📅 Calendar Generator

```bash
python calendar/calendar.py
```

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

* Learn Python programming.
* Explore useful third-party libraries.
* Build small but practical applications.
* Work with images, audio, video, and PDF files.
* Explore automation and multimedia processing.
* Improve problem-solving and programming skills.
* Experiment with different Python libraries and real-world use cases.

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository, make your changes, and submit a pull request.

## ⭐ Support

If you found this repository helpful, consider giving it a **⭐ Star** on GitHub.

Happy Coding! 🚀
