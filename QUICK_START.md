# 🚀 Alpha AI Assistant - Quick Start Guide

## ⚡ 5-Minute Setup (Hindi/English)

### Step 1: Install Termux (5 minutes)

1. **Download Termux from F-Droid** (NOT Play Store)
   - Go to: https://f-droid.org/repo/com.termux_118.apk
   - Install the APK

2. **Open Termux and grant permissions**
   ```bash
   termux-setup-storage
   ```
   - Click "ALLOW" when prompted

### Step 2: Install Alpha AI (3 minutes)

3. **Update Termux**
   ```bash
   pkg update && pkg upgrade -y
   ```

4. **Install git and Python**
   ```bash
   pkg install -y python python-pip git
   ```

5. **Clone Alpha AI from GitHub**
   ```bash
   git clone https://github.com/YOUR_USERNAME/alpha_ai_assistant.git
   cd alpha_ai_assistant
   ```

6. **Run installation script**
   ```bash
   chmod +x install.sh
   ./install.sh
   ```
   - This will take 5-10 minutes
   - Wait for completion

### Step 3: Start Alpha AI (1 minute)

7. **Start Alpha**
   ```bash
   python main.py
   ```

8. **Say "Alpha" to activate**
   - Alpha will respond: "Hello boss! Alpha is activated and ready to help!"

## 🎤 Basic Commands (Hindi)

### Apps Download (Apps Download करें)
- "Download Instagram app"
- "WhatsApp download karo"
- "Play Store se YouTube download karo"

### Web Search (वेब सर्च करें)
- "Google search Python tutorials"
- "Search latest news"
- "Weather in Delhi search karo"

### Phone Calls (फोन कॉल करें)
- "Call 9876543210"
- "Mummy ko call karo"
- "Dad ko call lagao"

### Messaging (मैसेज भेजें)
- "WhatsApp message to 9876543210 that says Hello"
- "Instagram message to friend that says Kya haal hai"
- "Send WhatsApp message to Mom"

### Camera (फोटो लें)
- "Take a photo"
- "Photo khecho"
- "Picture capture karo"

### YouTube (वीडियो चलाएं)
- "Play Despacito on YouTube"
- "YouTube pe Hindi songs chalao"
- "Play motivational videos"

### Screen Control (स्क्रीन कंट्रोल)
- "Scroll up"
- "Scroll down"
- "Screen neeche karo"

### Code Generation (कोड लिखें)
- "Write code for calculator"
- "Python code banao game ka"
- "Generate code for website"

### Stop Alpha (Alpha रोकें)
- "Stop Alpha"
- "Alpha stop karo"
- "Sleep"

## 🎨 Using the UI (UI का उपयोग)

### Floating Logo (तैरता हुआ लोगो)
1. **Drag the logo** - कहीं भी खींचें
2. **Click the logo** - Options देखने के लिए
3. **Blue background** - Alpha चालू है
4. **Gray background** - Alpha बंद है

### Control Buttons (कंट्रोल बटन)
- **▶ START** - Alpha शुरू करें
- **⏸ STOP** - Alpha रोकें
- **🗑 UNINSTALL** - Alpha हटाएं

## 📱 Complete Feature List

### ✅ Phone Control Features
- ✅ Play Store automation
- ✅ Google search
- ✅ Web browsing with paywall bypass
- ✅ Make/receive/reject calls
- ✅ WhatsApp messaging
- ✅ Instagram messaging
- ✅ Camera photo capture
- ✅ Screen scroll control
- ✅ YouTube video playback
- ✅ Auto-login to apps
- ✅ Code generation

### ✅ Voice Features
- ✅ Female voice (औरत की आवाज़)
- ✅ High accuracy recognition
- ✅ Natural language commands
- ✅ Hindi & English support

### ✅ UI Features
- ✅ Draggable floating logo
- ✅ Beautiful design
- ✅ Status indicators
- ✅ Easy controls

## 🔧 Troubleshooting (समस्या समाधान)

### Problem: Alpha won't start (Alpha नहीं चल रहा)
**Solution:**
```bash
cd ~/alpha_assistant
pip install -r requirements.txt
python main.py
```

### Problem: Voice not working (आवाज़ नहीं आ रही)
**Solution:**
```bash
pkg install ffmpeg
# Restart Termux
```

### Problem: Camera not working (कैमरा नहीं चल रहा)
**Solution:**
```bash
termux-setup-storage
# Grant camera permissions in settings
```

### Problem: Screen analysis not working (स्क्रीन एनालिसिस नहीं हो रहा)
**Solution:**
```bash
pkg install tesseract
# Restart Alpha
```

## 📞 Help & Support

### Check Logs (लॉग्स देखें)
```bash
cat alpha_log.txt
```

### Reinstall Alpha (Alpha फिर से इंस्टॉल करें)
```bash
cd ~/alpha_assistant
./uninstall.sh
# Then run install.sh again
```

### Get Help (मदद लें)
- Check README.md
- Check TERMUX_COMMANDS.md
- Open issue on GitHub

## 🎯 Pro Tips

1. **Always say "Alpha" first** - हमेशा पहले "Alpha" बोलें
2. **Speak clearly** - साफ़ बोलें
3. **Keep internet ON** - इंटरनेट चालू रखें
4. **Clear storage** - स्टोरेज खाली रखें
5. **Charge your phone** - फोन चार्ज करें

## 📝 Daily Usage Tips

### Morning Routine (सुबह की रूटीन)
```
"Alpha" → "Good morning Alpha"
"Play news on YouTube"
"Check WhatsApp messages"
```

### Work Mode (काम के मोड में)
```
"Alpha" → "Open Gmail"
"Search for project tutorials"
"Write code for calculator"
```

### Entertainment (मनोरंजन)
```
"Alpha" → "Play songs on YouTube"
"Scroll down"
"Take a photo"
```

### Evening (शाम)
```
"Alpha" → "Call Mom"
"Send WhatsApp message to friends"
"Stop Alpha"
```

## 🎉 You're Ready!

अब आप तैयार हैं! कहें "Alpha" और शुरू करें!

---

**🤖 Say "Alpha" and let your AI assistant help you! 🤖**

**Made with ❤️ by SuperNinja**

Need help? Check:
- README.md - Complete documentation
- TERMUX_COMMANDS.md - All commands
- GitHub issues - Community support