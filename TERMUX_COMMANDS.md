# Termux Commands Guide for Alpha AI Installation

## 📱 Basic Termux Setup Commands

### 1. Storage Permissions
```bash
termux-setup-storage
```
This gives Termux access to your phone's storage.

### 2. Update Packages
```bash
pkg update && pkg upgrade -y
```
Updates all Termux packages to the latest version.

### 3. Install Essential Packages
```bash
pkg install -y python python-pip git wget curl ffmpeg
```
Installs Python, pip, git, and other essential tools.

## 🐍 Python Commands

### Check Python Version
```bash
python --version
```

### Install Python Packages
```bash
pip install package_name
```

### Install Multiple Packages from requirements.txt
```bash
pip install -r requirements.txt
```

### Run Python Script
```bash
python main.py
```

### Run Python Script in Background
```bash
python main.py &
```

## 📦 Package Installation Commands

### Install Git
```bash
pkg install git
```

### Install OpenCV
```bash
pkg install libopencv
```

### Install Tesseract (OCR)
```bash
pkg install tesseract
```

### Install FFmpeg (for audio/video)
```bash
pkg install ffmpeg
```

## 📁 File Management Commands

### List Files
```bash
ls
ls -la    # Detailed list
```

### Change Directory
```bash
cd directory_name
cd ..     # Go back
cd ~      # Go to home
```

### Create Directory
```bash
mkdir directory_name
mkdir -p path/to/directory
```

### Copy File
```bash
cp source_file destination
cp -r source_dir destination_dir
```

### Move/Rename File
```bash
mv old_name new_name
mv file destination/
```

### Delete File
```bash
rm filename
rm -r directory_name    # Delete directory
rm -rf directory_name   # Force delete
```

### View File Content
```bash
cat filename
less filename
head filename    # First 10 lines
tail filename    # Last 10 lines
```

## 🔧 System Commands

### Check Running Processes
```bash
ps aux
```

### Kill Process
```bash
pkill process_name
kill -9 PID
```

### Check System Info
```bash
uname -a
```

### Check Disk Space
```bash
df -h
```

### Check Memory Usage
```bash
free -h
```

## 🌐 Network Commands

### Test Internet Connection
```bash
ping google.com
```

### Download File
```bash
wget URL
curl -O URL
```

### Check IP Address
```bash
ip addr show
```

## 📋 Git Commands

### Clone Repository
```bash
git clone repository_url
```

### Check Git Status
```bash
git status
```

### Add Files to Git
```bash
git add .
git add filename
```

### Commit Changes
```bash
git commit -m "Commit message"
```

### Push to GitHub
```bash
git push
git push -u origin main
```

### Pull from GitHub
```bash
git pull
```

## 🔐 Permission Commands

### Make Script Executable
```bash
chmod +x script.sh
```

### Change File Permissions
```bash
chmod 755 filename
chmod 644 filename
```

## 🚀 Alpha AI Specific Commands

### Install Alpha AI
```bash
cd alpha_assistant
chmod +x install.sh
./install.sh
```

### Start Alpha AI
```bash
cd alpha_assistant
python main.py
```

### Start Alpha AI in Background
```bash
cd alpha_assistant
nohup python main.py > alpha.log 2>&1 &
```

### Stop Alpha AI
```bash
pkill -f "python main.py"
```

### Check Alpha AI Status
```bash
ps aux | grep python
```

### Uninstall Alpha AI
```bash
cd alpha_assistant
chmod +x uninstall.sh
./uninstall.sh
```

## 🗑 Cleanup Commands

### Clear Python Cache
```bash
find . -type d -name "__pycache__" -exec rm -rf {} +
```

### Clear Package Cache
```bash
pkg clean
```

### Remove Unused Packages
```bash
pkg autoremove
```

## 📝 Text Editing Commands

### Edit File with nano
```bash
nano filename
```

### Edit File with vim
```bash
vim filename
```

### Edit File with micro
```bash
pkg install micro
micro filename
```

## 🔍 Search Commands

### Search for File
```bash
find / -name filename
find . -name "*.py"
```

### Search Text in Files
```bash
grep "search_term" filename
grep -r "search_term" directory
```

## 📊 Monitoring Commands

### Monitor CPU Usage
```bash
top
```

### Monitor Network
```bash
iftop
```

### Monitor Disk I/O
```bash
iotop
```

## 🎯 Useful Tips

### 1. Always update before installing
```bash
pkg update && pkg upgrade -y
```

### 2. Use -y flag for automatic yes
```bash
pkg install package -y
```

### 3. Run commands in background to keep terminal free
```bash
command &
```

### 4. Check if a command exists
```bash
which command
command -v command
```

### 5. Get help for any command
```bash
command --help
man command
```

## ⚠️ Important Notes

1. **Always run `termux-setup-storage` first** - This is crucial for accessing phone storage
2. **Use F-Droid version of Termux** - NOT the Play Store version
3. **Grant necessary permissions** - Microphone, storage, camera, etc.
4. **Keep Termux updated** - Regular updates ensure compatibility
5. **Use tmux for persistent sessions** - Keeps Alpha running even if terminal closes
   ```bash
   pkg install tmux
   tmux new -s alpha
   ```

## 🆘 Troubleshooting Commands

### If Python doesn't work
```bash
pkg uninstall python
pkg install python
```

### If pip doesn't work
```bash
python -m ensurepip --upgrade
pip install --upgrade pip
```

### If git doesn't work
```bash
pkg uninstall git
pkg install git
```

### Check logs
```bash
cat alpha_log.txt
tail -f alpha_log.txt    # Live monitoring
```

## 📞 Getting Help

If you encounter issues:
1. Check the logs in `alpha_log.txt`
2. Try updating packages: `pkg update && pkg upgrade`
3. Reinstall the specific package
4. Restart Termux completely
5. Check the README.md for more help

---

**🎯 Pro Tip:** Create aliases for frequently used commands in `~/.bashrc`:
```bash
echo "alias alpha='cd ~/alpha_assistant && python main.py'" >> ~/.bashrc
echo "alias alpha-stop='pkill -f python main.py'" >> ~/.bashrc
source ~/.bashrc
```

Now you can just type `alpha` to start and `alpha-stop` to stop!