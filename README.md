# 🎵 YouTube-Music-Extractor

A lightweight, loopable Python script that turns simple text searches into clean, beautifully named MP3 music files. No messy URLs required—just type the song name and let the script do the rest.

## ✨ Features
* **📂 Set and Forget Folder Path:** Prompts you once at launch for your download destination, then automatically saves everything there.
* **🔄 Endless Loop Mode:** Keeps running so you can download a whole playlist's worth of individual tracks without restarting the script.
* **🧼 Heavy-Duty Title Cleaner:** Uses regex to automatically strip out annoying video clutter like `(Official Video)`, `[HQ]`, `Lyrics`, `feat.`, and messy extra spaces.
* **⚡ Smart Skip:** Instantly checks your folder and skips downloads if the cleaned song title already exists.
* **🔒 Safe Filenames:** Automatically sanitizes illegal Windows/Mac filesystem characters (`\/:*?"<>|`).

## 🛠️ Quick Setup

### 1. Requirements
Make sure you have Python installed, then install the required `yt-dlp` package:
```bash
pip install yt-dlp

2. FFmpeg Installation (Required for MP3 Conversion)
This script requires FFmpeg to extract and convert the audio into high-quality MP3s.

🪟 Windows:
Download the FFmpeg essentials build from Gyan.dev.

Extract the folder and find ffmpeg.exe inside the bin folder.

Drop ffmpeg.exe directly into the same folder as this script. The script is pre-programmed to automatically look for it there!

🍏 Mac (Using Homebrew):
Open your terminal and run:

Bash
brew install ffmpeg
🐧 Linux:
Open your terminal and run:

Bash
sudo apt install ffmpeg
🚀 How to Use
Run the script:

Bash
python main.py
Enter the folder path where you want to save your music (or hit Enter to save it right next to the script).

Type any song name (e.g., Blinding Lights).

Type exit whenever you are done!
