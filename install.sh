#!/bin/bash

# Alpha AI Assistant - Installation Script for Android (Termux) - Fixed Version
# Created by SuperNinja

echo "========================================="
echo "🤖 ALPHA AI ASSISTANT INSTALLER 🤖"
echo "Fixed Version with Error Handling"
echo "========================================="
echo ""

# Update and upgrade packages
echo "📦 Updating Termux packages..."
pkg update && pkg upgrade -y || {
    echo "⚠️  Warning: Update failed, continuing anyway..."
}

# Install required Termux packages
echo "📦 Installing system dependencies..."
pkg install -y python python-pip git wget curl ffmpeg || {
    echo "❌ Error: Failed to install core packages"
    exit 1
}

# Install Termux API packages for settings control
echo "📦 Installing Termux API for settings control..."
pkg install -y termux-api || {
    echo "⚠️  Warning: Termux-API not installed. Settings control may not work."
    echo "💡 Install Termux-API from F-Droid for full functionality."
}

# Create Alpha directory
echo "📁 Creating Alpha directory..."
mkdir -p ~/alpha_assistant
cd ~/alpha_assistant

# Install Python packages with error handling
echo "📦 Installing Python packages..."
echo "⚠️  Note: Some packages may fail to install. Alpha will work without them."

# Install Flask (required)
echo "Installing Flask..."
pip install flask || echo "⚠️  Flask installation failed"

# Install optional packages
echo "Installing optional packages (may fail - that's OK)..."
pip install speechrecognition 2>/dev/null || echo "⚠️  SpeechRecognition not installed - Text input will be used"
pip install pyttsx3 2>/dev/null || echo "⚠️  pyttsx3 not installed - System TTS will be used"
pip install opencv-python 2>/dev/null || echo "⚠️  OpenCV not installed - Camera features disabled"
pip install Pillow 2>/dev/null || echo "⚠️  Pillow not installed - Image features disabled"
pip install numpy 2>/dev/null || echo "⚠️  NumPy not installed - Some features disabled"
pip install pyautogui 2>/dev/null || echo "⚠️  PyAutoGUI not installed - Screen automation disabled"
pip install requests 2>/dev/null || echo "⚠️  Requests not installed - Web features disabled"
pip install pytesseract 2>/dev/null || echo "⚠️  Tesseract not installed - OCR disabled"

# Install Termux extra keys for better input
echo "📦 Installing Termux:stylis..."
pkg install -y termux-adapter 2>/dev/null || true

# Create necessary directories
echo "📁 Creating Alpha directories..."
mkdir -p ~/alpha_assistant/screenshots
mkdir -p ~/alpha_assistant/codes
mkdir -p ~/alpha_assistant/logs
mkdir -p ~/alpha_assistant/moods
mkdir -p ~/alpha_assistant/settings
mkdir -p /sdcard/Alpha

# Copy UI files to accessible location
echo "📁 Setting up UI files..."
if [ -d "ui" ]; then
    cp -r ui/ /sdcard/Alpha/
fi

# Setup permissions
echo "🔧 Setting up permissions..."
chmod +x install.sh 2>/dev/null || true
chmod +x main.py 2>/dev/null || true

# Create launcher script
echo "🚀 Creating launcher script..."
cat > ~/start_alpha.sh << 'EOF'
#!/bin/bash
cd ~/alpha_assistant
echo "Starting Alpha AI Assistant..."
python main.py
EOF

chmod +x ~/start_alpha.sh

# Create desktop shortcut (optional)
echo "📱 Creating desktop shortcut..."
cat > ~/Desktop/Alpha.desktop << 'EOF' 2>/dev/null || true
[Desktop Entry]
Version=1.0
Type=Application
Name=Alpha AI
Comment=AI Assistant
Exec=~/start_alpha.sh
Icon=/sdcard/Alpha/icon.png
Terminal=true
EOF

echo ""
echo "========================================="
echo "✅ INSTALLATION COMPLETE! ✅"
echo "========================================="
echo ""
echo "To start Alpha AI:"
echo "  1. Open Termux"
echo "  2. Run: ~/start_alpha.sh"
echo "  or"
echo "  2. Run: cd ~/alpha_assistant && python main.py"
echo ""
echo "⚠️  Important Notes:"
echo "  - Some features may be limited if packages failed to install"
echo "  - Alpha will work with text input if voice recognition fails"
echo "  - Install Termux-API from F-Droid for settings control"
echo ""
echo "💡 To enable voice recognition, install these:"
echo "  pkg install pulseaudio"
echo "  pip install SpeechRecognition pyaudio"
echo ""
echo "Say 'Alpha' to activate your AI assistant!"
echo "========================================="