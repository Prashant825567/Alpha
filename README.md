# 🤖 Alpha AI Assistant - Female Voice AI for Android

A powerful AI personal assistant for Android phones with female voice control, screen analysis, and complete phone automation capabilities.

## ✨ Features

### 🎤 Voice Control
- **Female voice** with natural TTS (Text-to-Speech)
- Voice recognition with high accuracy
- Activate by saying "Alpha"
- Natural language commands
- **Text input fallback** if voice not available

### 🎭 Emotional Intelligence (NEW!)
- **10 Human-like Emotions** - Happy, Sad, Excited, Worried, etc.
- Emotion detection from voice
- Voice pitch and rate adjustment
- Emoji expressions
- Mood tracking
- Empathy and support
- Jokes and humor

### 📱 Phone Control
- **Play Store automation** - Download apps automatically
- **Google search** - Search anything on the web
- **Web browsing** - Open websites and bypass paywalls
- **Call management** - Make/receive/reject calls
- **WhatsApp messaging** - Send messages via WhatsApp
- **Instagram messaging** - Send DMs on Instagram
- **Camera access** - Take photos remotely
- **Screen control** - Scroll up/down, tap interactions
- **YouTube control** - Play videos and music
- **Auto-login** - Login to apps and websites
- **Code generation** - Write and execute code

### 🎛️ Settings Control (NEW!)
- **WiFi Control** - Turn on/off WiFi
- **Bluetooth Control** - Turn on/off Bluetooth
- **Volume Control** - Set 0-100%, up, down, mute, max
- **Brightness Control** - Set 0-100%, up, down, min, max
- **Do Not Disturb** - Turn on/off DND mode
- **Airplane Mode** - Turn on/off flight mode
- **Settings Status** - Check all current settings

### 🖼️ Screen Analysis
- Real-time screen content analysis
- OCR (Optical Character Recognition)
- Smart app selection
- Visual understanding

### 🎨 Beautiful UI
- **Draggable floating logo**
- Start/Stop/Uninstall controls
- Blue background when active
- Gray background when stopped
- Click for options

## 📋 Requirements

### Android Phone
- Android 7.0 or higher
- 2GB+ RAM
- 500MB+ free storage

### Termux App
- Install [Termux](https://f-droid.org/repo/com.termux_118.apk) from F-Droid (NOT Play Store)
- Allow storage permissions

## 🚀 Installation Guide

### Step 1: Install Termux
1. Download Termux from F-Droid
2. Open Termux
3. Grant storage permissions:
   ```bash
   termux-setup-storage
   ```

### Step 2: Clone or Download
**Option A: From GitHub**
```bash
# Install git
pkg install git

# Clone the repository
git clone https://github.com/YOUR_USERNAME/alpha_ai_assistant.git
cd alpha_ai_assistant
```

**Option B: Manual Download**
1. Download all files to your phone
2. Move files to Termux home directory
3. Navigate to the directory

### Step 3: Run Installation Script
```bash
# Make script executable
chmod +x install.sh

# Run installation
./install.sh
```

This will:
- Update Termux packages
- Install Python and required libraries
- Setup Alpha directories
- Configure permissions

### Step 4: Start Alpha AI
```bash
# Run Alpha
python main.py
```

Or use the launcher:
```bash
~/start_alpha.sh
```

## 🎮 Usage

### Starting Alpha
1. Open Termux
2. Run: `python main.py`
3. Say "Alpha" to activate
4. Alpha will respond: "Hello boss! Alpha is activated and ready to help!"

### Voice Commands

#### App Installation
- "Download Instagram app"
- "Download WhatsApp"
- Alpha will search Play Store and ask if multiple apps found

#### Web Search
- "Search for latest news"
- "Google Python tutorials"
- "Search weather in Delhi"

#### Website Access
- "Open youtube.com"
- "Open facebook"
- Alpha can bypass paywalls on some sites

#### Phone Calls
- "Call 9876543210"
- "Call Mom"
- "Call Dad"

#### Messaging
- "WhatsApp message to 9876543210 that says Hello"
- "Instagram message to johndoe that says How are you?"

#### Camera
- "Take a photo"
- "Capture a picture"
- "Click a photo"

#### Screen Control
- "Scroll up"
- "Scroll down"

#### YouTube
- "Play Despacito on YouTube"
- "Play Hindi songs on YouTube"
- "YouTube motivational videos"

#### Login
- "Login with myemail@gmail.com"
- "Login with 9876543210"

#### Code Generation
- "Write code for a calculator"
- "Generate code for a game"
- "Create a Python script for data analysis"

#### Stopping Alpha
- "Stop Alpha"
- "Sleep"

### Using the UI

1. **Floating Logo**: Drag the Alpha logo anywhere on screen
2. **Start Button**: Activates Alpha (blue background)
3. **Stop Button**: Deactivates Alpha (gray background)
4. **Uninstall Button**: Removes Alpha from your phone
5. **Emotion Display**: Shows current emotion with emoji

### Settings Control Commands

#### WiFi & Bluetooth
- "Turn on WiFi" / "Turn off WiFi"
- "Turn on Bluetooth" / "Turn off Bluetooth"

#### Volume Control
- "Set volume to 80%"
- "Volume up" / "Volume down"
- "Mute volume" / "Max volume"

#### Brightness Control
- "Set brightness to 70%"
- "Brightness up" / "Brightness down"
- "Brightness max" / "Brightness min"

#### Special Modes
- "Turn on Do Not Disturb"
- "Turn on Airplane Mode"
- "What are my current settings?"

See [SETTINGS_GUIDE.md](SETTINGS_GUIDE.md) for complete settings control documentation.

## 📁 Project Structure

```
alpha_assistant/
├── main.py              # Main Alpha AI code
├── install.sh           # Installation script
├── uninstall.sh         # Uninstallation script
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── ui/
│   └── alpha_ui.html   # Floating UI interface
├── screenshots/        # Screenshots storage
├── codes/              # Generated code storage
└── logs/               # Log files
```

## 🔧 Troubleshooting

### Alpha won't start
- Check if Python is installed: `python --version`
- Reinstall dependencies: `pip install -r requirements.txt`
- Check logs in `alpha_log.txt`

### Voice not working
- Check microphone permissions
- Ensure Termux has audio access
- Restart Termux

### Screen analysis not working
- Install Tesseract: `pkg install tesseract`
- Check storage permissions: `termux-setup-storage`

### Camera not working
- Grant camera permissions to Termux
- Check if camera is accessible

### Commands not recognized
- Speak clearly and slowly
- Check internet connection
- Ensure "Alpha" is spoken to activate

## 🔐 Permissions Required

- **Microphone**: For voice commands
- **Storage**: For saving codes and screenshots
- **Camera**: For taking photos
- **Internet**: For web searches and AI features
- **Phone**: For making calls
- **SMS**: For sending messages

## 📝 Notes

- **Always say "Alpha"** before giving commands
- **Speak clearly** for better recognition
- **Keep internet connection** for web features
- **Storage space**: Keep at least 500MB free
- **Battery**: Alpha runs in background, monitor battery usage

## 🗑 Uninstallation

### Using the Uninstall Script
```bash
cd ~/alpha_assistant
chmod +x uninstall.sh
./uninstall.sh
```

### Manual Uninstallation
```bash
# Stop Alpha
pkill -f "python main.py"

# Remove directories
rm -rf ~/alpha_assistant
rm -rf /sdcard/Alpha
rm -f ~/start_alpha.sh
```

## 🤝 Contributing

To contribute to Alpha AI:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available for personal and commercial use.

## 👨‍💻 Author

Created with ❤️ by SuperNinja

## 🙏 Acknowledgments

- Speech Recognition - Google Speech API
- TTS Engine - pyttsx3
- OCR - Tesseract
- Screen Automation - PyAutoGUI

## 📞 Support

For issues and questions:
- Open an issue on GitHub
- Check the troubleshooting section
- Review logs in `alpha_log.txt`

---

**🤖 Say "Alpha" and let your AI assistant help you! 🤖**

Made with ❤️ by SuperNinja