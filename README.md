# 🎥 Python Screen Recorder App

A lightweight and efficient **desktop screen recording application** built with **Python 3.12**, designed for Ubuntu systems.  
The app provides a simple GUI to capture screen activity and save recordings locally with minimal configuration.

---

## 🚀 Overview

This screen recorder application allows users to easily record their screen using a minimal interface.  
It is ideal for creating tutorials, recording demonstrations, or capturing on-screen activity without relying on heavy third-party software.

The application focuses on **simplicity, performance, and reliability**.

---

## ✨ Key Features

- 🖥️ Simple GUI with Start & Stop recording controls
- 🎬 Smooth screen capture using OpenCV & PyAutoGUI
- ⏱️ Automatic timestamp-based file naming
- 📁 Saves recordings in `.avi` format
- ⚡ Multi-threaded recording for smooth performance
- 🧠 Accurate time tracking using Python datetime

---

## 🛠️ Technology Stack

- **Python 3.12**
- **Tkinter** – GUI interface
- **OpenCV** – Video capture & processing
- **PyAutoGUI** – Screen capture
- **NumPy** – Frame processing
- **Threading** – Concurrent recording execution
- **Datetime** – Timestamp management

---

## 🖥️ Supported Platform

- **Ubuntu Linux**
- Designed to run inside a **Python virtual environment**

---

## 📂 Project Structure

```text
screen-recorder-app/
├── recorder.py
├── requirements.txt
├── README.md
```

## ⚙️ Installation & Setup

###  Clone the Repository

```bash
      git clone https://github.com/amarkumar55/Python-Screen-Recorder-App
      cd Python-Screen-Recorder-App
```
2️
### Create Virtual Environment

      python3 -m venv venv
      source venv/bin/activate
   
### Install Dependencies

     pip install -r requirements.txt

### Run the Application

    python recorder.py

📌 How It Works

      Click Start Recording to begin screen capture
      
      Perform any on-screen activity
      
      Click Stop Recording
   
      Video is saved automatically with a timestamped filename

🎯 Use Cases

      Creating tutorials
      
      Recording demos or presentations
      
      Capturing system behavior
      
      Educational screen recordings

### Learning Highlights

      Desktop application development with Python
      
      Multi-threaded screen capture
      
      OpenCV video processing
      
      GUI design with Tkinter
      
      Linux-based application setup

### License

     This project is intended for educational and personal use.

     
