# 🎥 Python Screen Recorder App
### Lightweight desktop screen recording · Python · OpenCV · Multi-threaded · Ubuntu

![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat-square&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Video_Capture-5C3EE8?style=flat-square&logo=opencv)
![Platform](https://img.shields.io/badge/Platform-Ubuntu_Linux-E95420?style=flat-square&logo=ubuntu)
![GUI](https://img.shields.io/badge/GUI-Tkinter-lightgrey?style=flat-square)
![License](https://img.shields.io/badge/License-Personal_Use-lightgrey?style=flat-square)

> A minimal, multi-threaded desktop screen recorder built in Python — no heavy third-party software, no configuration overhead. Start recording in one click, get a timestamped `.avi` file when you stop.

---

## ✨ Features

- 🖥️ Simple GUI — Start & Stop recording controls via Tkinter
- 🎬 Smooth screen capture using OpenCV + PyAutoGUI
- ⚡ Multi-threaded recording — UI stays responsive during capture
- ⏱️ Automatic timestamp-based file naming — no manual saving
- 📁 Output saved as `.avi` — compatible with standard video players
- 🧠 Accurate time tracking via Python `datetime`

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.12 | Core runtime |
| Tkinter | GUI — start/stop controls |
| OpenCV | Video frame capture and encoding |
| PyAutoGUI | Screen screenshot per frame |
| NumPy | Frame array processing |
| Threading | Concurrent recording — non-blocking UI |
| Datetime | Timestamped output filenames |

---

## ⚙️ How It Works

```
User clicks Start
        │
        ▼
Background thread launches (non-blocking)
        │
        ▼
PyAutoGUI captures screen → NumPy array → OpenCV encodes frame
        │
        ▼
Frames written to .avi file in real time
        │
        ▼
User clicks Stop → thread joins → file saved with timestamp
```

**Why multi-threading?** Running the capture loop on the main thread would freeze the GUI. A background thread keeps the interface responsive while recording runs continuously in parallel.

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/amarkumar55/Python-Screen-Recorder-App
cd Python-Screen-Recorder-App

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python recorder.py
```

### Usage
1. Click **Start Recording** — capture begins immediately
2. Perform any on-screen activity
3. Click **Stop Recording** — video saved automatically as `recording_YYYYMMDD_HHMMSS.avi`

---

## 📁 Project Structure

```
screen-recorder-app/
├── recorder.py          # Main app — GUI + recording logic + threading
├── requirements.txt     # opencv-python, pyautogui, numpy
└── README.md
```

---

## 🖥️ Platform

- **Ubuntu Linux** — tested on Ubuntu with Python 3.12
- Runs inside a Python virtual environment
- No system-level dependencies beyond pip packages

---

## 🌍 Use Cases

- Creating software tutorials and walkthroughs
- Recording demos and presentations
- Capturing system behavior for bug reports
- Educational screen recordings without third-party tools

---

## 🔭 Roadmap

- [ ] Audio recording support (microphone overlay)
- [ ] MP4 output format (better compression than AVI)
- [ ] Region selection — record a specific area of the screen
- [ ] Windows and macOS support
- [ ] Hotkey support for start/stop without clicking

---

## 👤 Author

**Amar Kumar** — Senior Backend Engineer · IBM Certified AI Engineer  
📌 [LinkedIn](https://www.linkedin.com/in/amarkumar241429017) · 💻 [GitHub](https://github.com/amarkumar55)

---

*Simple tools built well — multi-threading, clean separation of UI and capture logic, zero external dependencies beyond pip.*
