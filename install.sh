#!/bin/bash

# Alpha AI Assistant - Installation Script for Android (Termux)
# Created by SuperNinja

echo "========================================="
echo "🤖 ALPHA AI ASSISTANT INSTALLER 🤖"
echo "========================================="
echo ""

# Update and upgrade packages
echo "📦 Updating Termux packages..."
pkg update && pkg upgrade -y

# Install required Termux packages
echo "📦 Installing system dependencies..."
pkg install -y python python-pip git wget curl ffmpeg

# Install system libraries
echo "📦 Installing system libraries..."
pkg install -y libopencv tesseract

# Create Alpha directory
echo "📁 Creating Alpha directory..."
mkdir -p ~/alpha_assistant
cd ~/alpha_assistant

# Clone or create the project (assuming files are already present or user will copy)
echo "📥 Setting up Alpha AI files..."
# If files are not present, user should copy them or use git

# Install Python dependencies
echo "📦 Installing Python packages..."
pip install --upgrade pip
pip install -r requirements.txt

# Create necessary directories
echo "📁 Creating Alpha directories..."
mkdir -p ~/alpha_assistant/screenshots
mkdir -p ~/alpha_assistant/codes
mkdir -p ~/alpha_assistant/logs

# Copy UI files to accessible location
echo "📁 Setting up UI files..."
mkdir -p /sdcard/Alpha
cp -r ui/ /sdcard/Alpha/

# Setup permissions
echo "🔧 Setting up permissions..."
chmod +x install.sh
chmod +x main.py

# Create launcher script
echo "🚀 Creating launcher script..."
cat > ~/start_alpha.sh << 'EOF'
#!/bin/bash
cd ~/alpha_assistant
python main.py
EOF

chmod +x ~/start_alpha.sh

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
echo "Say 'Alpha' to activate your AI assistant!"
echo "========================================="