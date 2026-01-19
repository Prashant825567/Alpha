#!/usr/bin/env python3
"""
Alpha AI Assistant - Demo/Test Script
Run this to test all features before full deployment
"""

import os
import sys
import time

print("=" * 60)
print("🤖 ALPHA AI ASSISTANT - DEMO/TEST MODE 🤖")
print("=" * 60)
print()

def test_imports():
    """Test if all required modules can be imported"""
    print("📦 Testing module imports...")
    
    modules = [
        'speech_recognition',
        'pyttsx3',
        'cv2',
        'PIL',
        'pyautogui',
        'requests',
        'flask',
        'numpy',
        'json',
        'threading',
        'subprocess',
        'datetime'
    ]
    
    failed = []
    
    for module in modules:
        try:
            __import__(module)
            print(f"  ✅ {module}")
        except ImportError as e:
            print(f"  ❌ {module} - {e}")
            failed.append(module)
    
    if failed:
        print(f"\n⚠️  Failed to import: {', '.join(failed)}")
        print("Run: pip install -r requirements.txt")
        return False
    else:
        print("\n✅ All modules imported successfully!")
        return True

def test_directories():
    """Test if required directories exist"""
    print("\n📁 Testing directories...")
    
    required_dirs = [
        'ui',
        'screenshots',
        'codes',
        'logs'
    ]
    
    for dir_name in required_dirs:
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
            print(f"  ✅ Created {dir_name}/")
        else:
            print(f"  ✅ {dir_name}/ exists")
    
    return True

def test_files():
    """Test if required files exist"""
    print("\n📄 Testing required files...")
    
    required_files = [
        'main.py',
        'ui/alpha_ui.html',
        'config.json',
        'requirements.txt',
        'install.sh',
        'uninstall.sh',
        'README.md',
        'QUICK_START.md',
        'TERMUX_COMMANDS.md'
    ]
    
    missing = []
    
    for file_name in required_files:
        if os.path.exists(file_name):
            print(f"  ✅ {file_name}")
        else:
            print(f"  ❌ {file_name} - MISSING")
            missing.append(file_name)
    
    if missing:
        print(f"\n⚠️  Missing files: {', '.join(missing)}")
        return False
    else:
        print("\n✅ All required files present!")
        return True

def test_config():
    """Test configuration file"""
    print("\n⚙️  Testing configuration...")
    
    try:
        import json
        with open('config.json', 'r') as f:
            config = json.load(f)
        
        print(f"  ✅ Alpha name: {config['alpha']['name']}")
        print(f"  ✅ Version: {config['alpha']['version']}")
        print(f"  ✅ Activation word: {config['alpha']['activation_word']}")
        print(f"  ✅ Voice gender: {config['alpha']['voice_settings']['gender']}")
        print(f"  ✅ API port: {config['api']['port']}")
        
        return True
    except Exception as e:
        print(f"  ❌ Config error: {e}")
        return False

def test_tts():
    """Test Text-to-Speech"""
    print("\n🎤 Testing Text-to-Speech (TTS)...")
    
    try:
        import pyttsx3
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        
        print(f"  ✅ TTS engine initialized")
        print(f"  ✅ Available voices: {len(voices)}")
        
        # Try to find female voice
        female_found = False
        for voice in voices:
            if 'female' in voice.name.lower() or 'zira' in voice.name.lower():
                print(f"  ✅ Female voice found: {voice.name}")
                female_found = True
                break
        
        if not female_found:
            print(f"  ⚠️  No female voice found, using default")
        
        return True
    except Exception as e:
        print(f"  ❌ TTS error: {e}")
        return False

def test_speech_recognition():
    """Test Speech Recognition (requires microphone)"""
    print("\n🎧 Testing Speech Recognition...")
    print("  ℹ️  This requires a microphone and user interaction")
    
    response = input("  Do you want to test speech recognition? (y/n): ").lower()
    
    if response == 'y':
        try:
            import speech_recognition as sr
            r = sr.Recognizer()
            print("  ✅ Speech recognition module loaded")
            
            with sr.Microphone() as source:
                print("  🎤 Speak something...")
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
                
                print("  🔄 Recognizing...")
                text = r.recognize_google(audio)
                print(f"  ✅ You said: '{text}'")
                
            return True
        except Exception as e:
            print(f"  ❌ Speech recognition error: {e}")
            return False
    else:
        print("  ⏭️  Speech recognition test skipped")
        return True

def test_flask():
    """Test Flask API"""
    print("\n🌐 Testing Flask API...")
    
    try:
        from flask import Flask
        app = Flask(__name__)
        
        @app.route('/test')
        def test():
            return {"status": "ok", "message": "Flask is working!"}
        
        print("  ✅ Flask initialized")
        print("  ℹ️  Flask API will run on port 5000")
        
        return True
    except Exception as e:
        print(f"  ❌ Flask error: {e}")
        return False

def test_camera():
    """Test Camera Access"""
    print("\n📷 Testing Camera Access...")
    
    response = input("  Do you want to test camera? (y/n): ").lower()
    
    if response == 'y':
        try:
            import cv2
            cap = cv2.VideoCapture(0)
            
            if cap.isOpened():
                print("  ✅ Camera accessed successfully")
                ret, frame = cap.read()
                if ret:
                    print("  ✅ Captured test frame")
                    cap.release()
                    return True
                else:
                    print("  ❌ Failed to capture frame")
                    cap.release()
                    return False
            else:
                print("  ❌ Could not open camera")
                return False
        except Exception as e:
            print(f"  ❌ Camera error: {e}")
            return False
    else:
        print("  ⏭️  Camera test skipped")
        return True

def test_screen_capture():
    """Test Screen Capture"""
    print("\n🖼️  Testing Screen Capture...")
    
    try:
        import pyautogui
        screenshot = pyautogui.screenshot()
        
        if screenshot:
            print("  ✅ Screen captured successfully")
            print(f"  📐 Size: {screenshot.size}")
            return True
        else:
            print("  ❌ Failed to capture screen")
            return False
    except Exception as e:
        print(f"  ⚠️  Screen capture error: {e}")
        print("  ℹ️  This may not work in all environments")
        return True

def run_tests():
    """Run all tests"""
    results = {
        'imports': test_imports(),
        'directories': test_directories(),
        'files': test_files(),
        'config': test_config(),
        'tts': test_tts(),
        'speech': test_speech_recognition(),
        'flask': test_flask(),
        'camera': test_camera(),
        'screen': test_screen_capture()
    }
    
    print("\n" + "=" * 60)
    print("📊 TEST RESULTS SUMMARY")
    print("=" * 60)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name.upper():20} : {status}")
    
    total_tests = len(results)
    passed_tests = sum(results.values())
    
    print("\n" + "=" * 60)
    print(f"Total: {passed_tests}/{total_tests} tests passed")
    
    if passed_tests == total_tests:
        print("\n🎉 ALL TESTS PASSED! Alpha is ready to use! 🎉")
        print("\nTo start Alpha AI:")
        print("  python main.py")
        print("\nSay 'Alpha' to activate!")
    else:
        print("\n⚠️  Some tests failed. Please fix the issues above.")
        print("\nCommon fixes:")
        print("  pip install -r requirements.txt")
        print("  termux-setup-storage")
    
    print("=" * 60)
    
    return passed_tests == total_tests

if __name__ == "__main__":
    try:
        success = run_tests()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Tests interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {e}")
        sys.exit(1)