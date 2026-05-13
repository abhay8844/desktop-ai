# Zira - AI Desktop Assistant

Zira is a Python-based intelligent AI desktop assistant designed to help you automate everyday tasks, search the web, control your system, and much more, right from your desktop.

## Features

- **Voice Interaction:** Listens to your voice commands and replies via text-to-speech.
- **System Control:** Control volume, pause/play media, mute, and capture screenshots.
- **Application Management:** Open and close desktop applications seamlessly.
- **Web Browsing & Search:** Search Google, YouTube, and Wikipedia through voice commands.
- **Utilities:**
  - Calculate math problems or fetch facts using WolframAlpha.
  - Test internet speed (download & upload).
  - Fetch current weather and temperature.
  - Set alarms and read out the current time and date.
  - Send WhatsApp messages.
  - Language translation.
  - Remember tasks and read them back to you.

## Prerequisites and Installation

To run Zira, you need Python installed on your system. It is recommended to use a virtual environment.

First, clone this repository or download the source code.

Then, install the necessary Python dependencies using `pip`:

```bash
pip install pyttsx3 SpeechRecognition wikipedia requests beautifulsoup4 plyer pyautogui speedtest-cli pywhatkit wolframalpha googletrans==4.0.0-rc1 gTTS playsound pynput opencv-python openai numpy
```

*Note: Some libraries, like `pyaudio` (required by `SpeechRecognition`), might require additional system dependencies depending on your OS.*

## Configuration / API Keys

Several features in Zira rely on external APIs. You **must** provide your own API keys for these functionalities to work.

1. **WolframAlpha API Key**:
   - Get a free API key from [WolframAlpha Developer Portal](https://developer.wolframalpha.com/).
   - Update `Calculatenumbers.py` to include your key:
     ```python
     apikey = "YOUR_WOLFRAMALPHA_API_KEY"
     ```
2. **OpenAI API Key (Optional / Advanced)**:
   - Some auxiliary scripts (`Openaitest.py`, `open.py`, `Nvidiaopenai.py`, `abhay.py`) are structured to interface with OpenAI or NVIDIA APIs.
   - If you plan to use these, update the `apikey1` variable or the `openai.api_key` in the respective scripts with your actual API credentials.

## Usage

Once all the dependencies are installed and the API keys are configured, you can start Zira by simply running the main file:

```bash
python main.py
```

- Say **"Wake up"** to start the main interaction loop.
- Zira will listen to your commands and perform actions like "Open YouTube", "Search Google for python programming", "Volume up", "What is the internet speed?", "Calculate 5 times 10", and more.
- When you are done, simply say **"Go to sleep"** or **"Shutdown the system"**.

---
*Developed as a desktop AI mini-project.*