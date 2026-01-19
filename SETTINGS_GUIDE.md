# 🎛️ Alpha AI - Phone Settings Control Guide

## 📋 Complete Settings Control Features

Alpha AI can now control your Android phone settings completely! Control WiFi, Bluetooth, Volume, Brightness, and more with voice commands.

---

## 🔌 WiFi Control

### Turn On WiFi
```
"Turn on WiFi"
"WiFi on"
"Enable WiFi"
"Alpha, please turn on WiFi"
```

### Turn Off WiFi
```
"Turn off WiFi"
"WiFi off"
"Disable WiFi"
"Alpha, please turn off WiFi"
```

**Response:**
- On: "WiFi has been turned on, boss! 📶"
- Off: "WiFi has been turned off, boss! 📵"

---

## 📡 Bluetooth Control

### Turn On Bluetooth
```
"Turn on Bluetooth"
"Bluetooth on"
"Enable Bluetooth"
"Alpha, please turn on Bluetooth"
```

### Turn Off Bluetooth
```
"Turn off Bluetooth"
"Bluetooth off"
"Disable Bluetooth"
"Alpha, please turn off Bluetooth"
```

**Response:**
- On: "Bluetooth has been turned on, boss! 📡"
- Off: "Bluetooth has been turned off, boss! 🔇"

---

## 🔊 Volume Control

### Set Specific Volume (0-100%)
```
"Set volume to 80%"
"Volume 50"
"Volume 100"
"Set volume to 30%"
```

### Volume Up
```
"Volume up"
"Increase volume"
"Make it louder"
"Volume up please"
```

### Volume Down
```
"Volume down"
"Decrease volume"
"Make it quieter"
"Volume down please"
```

### Mute Volume
```
"Mute volume"
"Volume mute"
"Silent mode"
"Mute please"
```

### Maximum Volume
```
"Max volume"
"Maximum volume"
"Volume to the max"
"Full volume"
```

**Responses:**
- Specific: "Volume has been set to 80%, boss! 🔊"
- Up: "Volume increased to 60%, boss! 🔊"
- Down: "Volume decreased to 40%, boss! 🔉"
- Mute: "Volume has been muted, boss! 🔇"
- Max: "Volume has been set to maximum, boss! 🔊"

---

## ☀️ Brightness Control

### Set Specific Brightness (0-100%)
```
"Set brightness to 80%"
"Brightness 50"
"Brightness 100"
"Set brightness to 30%"
"Brightness 20%"
```

### Brightness Up
```
"Brightness up"
"Increase brightness"
"Make it brighter"
"Brightness up please"
```

### Brightness Down
```
"Brightness down"
"Decrease brightness"
"Make it dimmer"
"Brightness down please"
```

### Maximum Brightness
```
"Max brightness"
"Maximum brightness"
"Brightness to the max"
"Highest brightness"
```

### Minimum Brightness
```
"Min brightness"
"Minimum brightness"
"Brightness to the min"
"Lowest brightness"
```

**Responses:**
- Specific: "Brightness has been set to 80%, boss! ☀️"
- Up: "Brightness increased, boss! ☀️"
- Down: "Brightness decreased, boss! 🌙"
- Max: "Brightness has been set to maximum, boss! ☀️"
- Min: "Brightness has been set to minimum, boss! 🌙"

---

## 🔕 Do Not Disturb Mode

### Turn On DND
```
"Turn on Do Not Disturb"
"DND on"
"Enable Do Not Disturb"
"Silent mode on"
"Don't disturb me"
```

### Turn Off DND
```
"Turn off Do Not Disturb"
"DND off"
"Disable Do Not Disturb"
"Silent mode off"
"You can disturb me now"
```

**Response:**
- On: "Do Not Disturb mode has been turned on, boss! 🔕"
- Off: "Do Not Disturb mode has been turned off, boss! 🔔"

---

## ✈️ Airplane Mode

### Turn On Airplane Mode
```
"Turn on Airplane Mode"
"Airplane mode on"
"Flight mode on"
"Enable airplane mode"
```

### Turn Off Airplane Mode
```
"Turn off Airplane Mode"
"Airplane mode off"
"Flight mode off"
"Disable airplane mode"
```

**Response:**
- On: "Airplane mode has been turned on, boss! ✈️"
- Off: "Airplane mode has been turned off, boss! 📶"

---

## 📊 Get Current Settings Status

### Check All Settings
```
"What are my current settings?"
"Tell me my settings"
"Settings status"
"Current settings status"
"Alpha, what's my settings?"
```

**Response:**
"Here are your current settings, boss: WiFi is on, Bluetooth is off, volume is at 80%, brightness is at 50%, and Do Not Disturb is off."

---

## 🎯 Practical Usage Examples

### Morning Routine
```
You: "Alpha"
Alpha: "Good morning, boss! ☀️ Ready to start an amazing day?"

You: "Set volume to 60%"
Alpha: "Volume has been set to 60%, boss! 🔊"

You: "Turn on WiFi"
Alpha: "WiFi has been turned on, boss! 📶"

You: "Set brightness to 70%"
Alpha: "Brightness has been set to 70%, boss! ☀️"
```

### Night Routine
```
You: "Alpha, turn on Do Not Disturb"
Alpha: "Do Not Disturb mode has been turned on, boss! 🔕"

You: "Set volume to 20%"
Alpha: "Volume has been set to 20%, boss! 🔊"

You: "Brightness to minimum"
Alpha: "Brightness has been set to minimum, boss! 🌙"

You: "Turn off Bluetooth"
Alpha: "Bluetooth has been turned off, boss! 🔇"
```

### Watching Videos
```
You: "Max brightness"
Alpha: "Brightness has been set to maximum, boss! ☀️"

You: "Max volume"
Alpha: "Volume has been set to maximum, boss! 🔊"

You: "Turn off notifications"
Alpha: "Do Not Disturb mode has been turned on, boss! 🔕"
```

### Meeting Mode
```
You: "Mute volume"
Alpha: "Volume has been muted, boss! 🔇"

You: "Turn on DND"
Alpha: "Do Not Disturb mode has been turned on, boss! 🔕"

You: "Turn off Bluetooth"
Alpha: "Bluetooth has been turned off, boss! 🔇"
```

---

## 🔧 Requirements

### Termux-API Package
For settings control to work, you need Termux-API installed:

1. **Download Termux-API from F-Droid**
   - Go to: https://f-droid.org/repo/com.termux.api_51.apk
   - Install the APK

2. **Grant Permissions**
   - Open Termux
   - Run: `termux-setup-storage`
   - Grant all requested permissions:
     - Modify system settings
     - Bluetooth
     - WiFi
     - Camera
     - Microphone
     - Location

3. **Test Settings Control**
   ```bash
   # Test WiFi
   termux-wifi-connection enable
   
   # Test Bluetooth
   termux-bluetooth enable
   
   # Test Volume
   termux-volume music 50
   
   # Test Brightness
   termux-brightness 128
   ```

---

## ⚠️ Troubleshooting

### Problem: Settings Control Not Working

**Solution 1: Install Termux-API**
```bash
# Download from F-Droid
https://f-droid.org/repo/com.termux.api_51.apk

# Grant permissions
termux-setup-storage
```

**Solution 2: Grant Permission in Android Settings**
1. Go to Android Settings
2. Apps → Termux
3. Permissions
4. Grant all permissions

**Solution 3: Use ADB Commands (Root Required)**
```bash
# Turn on WiFi
adb shell svc wifi enable

# Turn on Bluetooth
adb shell svc bluetooth enable

# Set volume
adb shell cmd media_session volume --stream 3 --set 50
```

### Problem: Volume Control Not Working

**Solution:**
```bash
# Check if audio service is running
pkg install pulseaudio
pulseaudio --start

# Test volume control
termux-volume music 50
```

### Problem: Brightness Control Not Working

**Solution:**
```bash
# Grant write settings permission
termux-setup-storage

# Use alternative method
adb shell settings put system screen_brightness 128
```

---

## 🎮 Advanced Settings Control

### Combination Commands
You can combine multiple settings in one command:

```
"Turn off WiFi and Bluetooth"
"Mute volume and turn on DND"
"Max brightness and max volume"
```

### Smart Suggestions
Alpha will suggest settings based on context:

- **Morning**: Suggests turning on WiFi, setting moderate brightness
- **Night**: Suggests turning on DND, lowering brightness
- **Meeting**: Suggests muting volume, enabling DND
- **Watching Videos**: Suggests max brightness and volume

---

## 📱 Settings API

You can also control settings programmatically:

### Get Current Settings
```bash
curl http://localhost:5000/api/settings/status
```

### Set WiFi
```bash
curl -X POST http://localhost:5000/api/settings/wifi \
  -H "Content-Type: application/json" \
  -d '{"action": "on"}'
```

### Set Volume
```bash
curl -X POST http://localhost:5000/api/settings/volume \
  -H "Content-Type: application/json" \
  -d '{"level": 80}'
```

### Set Brightness
```bash
curl -X POST http://localhost:5000/api/settings/brightness \
  -H "Content-Type: application/json" \
  -d '{"level": 70}'
```

---

## 🌟 Features Summary

### ✅ Supported Settings
- ✅ WiFi (On/Off)
- ✅ Bluetooth (On/Off)
- ✅ Volume (0-100%, Up, Down, Mute, Max)
- ✅ Brightness (0-100%, Up, Down, Min, Max)
- ✅ Do Not Disturb (On/Off)
- ✅ Airplane Mode (On/Off)
- ✅ Settings Status Check

### ✅ Voice Commands
- ✅ Natural language commands
- ✅ Multiple ways to say same thing
- ✅ Emotional responses
- ✅ Confirmation messages

### ✅ Error Handling
- ✅ Graceful fallback if permission denied
- ✅ Clear error messages
- ✅ Helpful suggestions
- ✅ Permission guidance

---

## 💡 Tips for Best Experience

1. **Install Termux-API**: Required for settings control
2. **Grant All Permissions**: WiFi, Bluetooth, etc.
3. **Speak Clearly**: For better voice recognition
4. **Use Specific Values**: "Volume 80%" works better than "Volume up a bit"
5. **Check Settings Status**: Use "What are my settings?" regularly

---

## 🚀 Quick Reference

### Volume
- "Volume 80%" - Set to 80%
- "Volume up" - Increase by 10%
- "Volume down" - Decrease by 10%
- "Mute" - Set to 0%
- "Max volume" - Set to 100%

### Brightness
- "Brightness 80%" - Set to 80%
- "Brightness up" - Increase
- "Brightness down" - Decrease
- "Brightness max" - Set to 100%
- "Brightness min" - Set to 0%

### WiFi & Bluetooth
- "WiFi on/off" - Control WiFi
- "Bluetooth on/off" - Control Bluetooth

### Modes
- "Do Not Disturb on/off" - DND mode
- "Airplane mode on/off" - Flight mode

---

**🎛️ Control your phone completely with voice commands!**

**Made with ❤️ by SuperNinja**

For issues, check TERMUX_COMMANDS.md or create a GitHub issue!