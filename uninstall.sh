#!/bin/bash

# Alpha AI Assistant - Uninstallation Script for Android (Termux)
# Created by SuperNinja

echo "========================================="
echo "🗑 ALPHA AI ASSISTANT UNINSTALLER 🗑"
echo "========================================="
echo ""

# Stop Alpha if running
echo "⏹ Stopping Alpha AI..."
pkill -f "python main.py" 2>/dev/null
pkill -f "python3 main.py" 2>/dev/null

# Ask for confirmation
echo ""
read -p "Are you sure you want to uninstall Alpha AI? (yes/no): " confirm

if [ "$confirm" != "yes" ]; then
    echo "Uninstallation cancelled."
    exit 0
fi

echo ""
echo "🗑 Removing Alpha AI files..."

# Remove Alpha directories
rm -rf ~/alpha_assistant
rm -rf /sdcard/Alpha
rm -f ~/start_alpha.sh

# Remove Python packages (optional)
echo ""
read -p "Do you want to remove Python packages too? (yes/no): " remove_packages

if [ "$remove_packages" = "yes" ]; then
    echo "📦 Uninstalling Python packages..."
    pip uninstall -y speechrecognition pyttsx3 opencv-python Pillow pyautogui requests flask numpy pytesseract selenium pyaudio
fi

echo ""
echo "========================================="
echo "✅ ALPHA AI HAS BEEN UNINSTALLED! ✅"
echo "========================================="
echo ""
echo "To reinstall Alpha AI:"
echo "  1. Go to your GitHub repository"
echo "  2. Clone the project again"
echo "  3. Run the install.sh script"
echo ""
echo "Thank you for using Alpha AI! 🤖"
echo "========================================="