#!/usr/bin/env python3
"""
Alpha AI Assistant - Female Voice AI Personal Assistant for Android with Human-like Emotions
Created with love by SuperNinja
"""

import os
import sys
import time
import json
import threading
import subprocess

# Try to import speech_recognition, provide fallback if not available
try:
    import speech_recognition as sr
    SR_AVAILABLE = True
except ImportError:
    SR_AVAILABLE = False
    print("⚠️  SpeechRecognition not installed. Voice commands will use text input.")

# Try to import pyttsx3, provide fallback if not available
try:
    import pyttsx3
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False
    print("⚠️  pyttsx3 not installed. Using system TTS.")

from datetime import datetime
import re
import random

# Try to import optional packages with fallbacks
try:
    import cv2
    CV2_AVAILABLE = True
except ImportError:
    CV2_AVAILABLE = False
    print("⚠️  OpenCV not installed. Camera features disabled.")

try:
    import numpy as np
    NUMPY_AVAILABLE = True
except ImportError:
    NUMPY_AVAILABLE = False
    print("⚠️  NumPy not installed. Some features disabled.")

try:
    from PIL import Image
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False
    print("⚠️  Pillow not installed. Image features disabled.")

try:
    import pyautogui
    AUTOGUI_AVAILABLE = True
except ImportError:
    AUTOGUI_AVAILABLE = False
    print("⚠️  PyAutoGUI not installed. Screen automation disabled.")

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False
    print("⚠️  Requests not installed. Web features disabled.")

from flask import Flask, request, jsonify
import webbrowser

# Initialize Flask for web control
app = Flask(__name__)

# Global State
alpha_state = {
    'is_running': False,
    'is_listening': False,
    'voice_enabled': True,
    'current_emotion': 'neutral',  # Current emotion state
    'mood_history': [],  # Track mood over time
    'user_name': 'boss',  # Default user name
    'last_interaction_time': None,
    'log_file': 'alpha_log.txt'
}

# Initialize TTS Engine with female voice
def init_tts():
    """Initialize Text-to-Speech with female voice"""
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        
        # Try to find female voice
        for voice in voices:
            if 'female' in voice.name.lower() or 'zira' in voice.name.lower():
                engine.setProperty('voice', voice.id)
                break
            elif 'microsoft' in voice.name.lower() and 'desktop' in voice.name.lower():
                engine.setProperty('voice', voice.id)
        
        # Set properties for natural female voice
        engine.setProperty('rate', 150)    # Speed
        engine.setProperty('volume', 0.9)  # Volume
        
        return engine
    except Exception as e:
        log_error(f"TTS initialization error: {e}")
        return None

tts_engine = init_tts()

# Initialize Speech Recognition
if SR_AVAILABLE:
    recognizer = sr.Recognizer()
else:
    recognizer = None

# ============================================
# PHONE SETTINGS CONTROL SYSTEM
# ============================================

class SettingsControl:
    """Control Android phone settings - WiFi, Bluetooth, Volume, Brightness"""
    
    def __init__(self):
        self.settings_file = '/storage/emulated/0/Alpha/settings_state.json'
        self.load_settings()
    
    def load_settings(self):
        """Load current settings state"""
        try:
            if os.path.exists(self.settings_file):
                with open(self.settings_file, 'r') as f:
                    self.settings = json.load(f)
            else:
                self.settings = {
                    'wifi': False,
                    'bluetooth': False,
                    'volume': 50,
                    'brightness': 50,
                    'do_not_disturb': False,
                    'airplane_mode': False
                }
        except Exception as e:
            log_error(f"Error loading settings: {e}")
            self.settings = {}
    
    def save_settings(self):
        """Save current settings state"""
        try:
            os.makedirs(os.path.dirname(self.settings_file), exist_ok=True)
            with open(self.settings_file, 'w') as f:
                json.dump(self.settings, f, indent=2)
        except Exception as e:
            log_error(f"Error saving settings: {e}")
    
    def wifi_control(self, action):
        """Control WiFi - on/off"""
        try:
            if action.lower() in ['on', 'enable', 'turn on']:
                # Turn on WiFi
                os.system("termux-wifi-connection enable")
                self.settings['wifi'] = True
                self.save_settings()
                speak("WiFi has been turned on, boss! 📶", emotion='happy')
                return True
            elif action.lower() in ['off', 'disable', 'turn off']:
                # Turn off WiFi
                os.system("termux-wifi-connection disable")
                self.settings['wifi'] = False
                self.save_settings()
                speak("WiFi has been turned off, boss! 📵", emotion='neutral')
                return True
        except Exception as e:
            log_error(f"WiFi control error: {e}")
            speak("Sorry boss, I couldn't control WiFi. You might need to grant permission.", emotion='worried')
            return False
    
    def bluetooth_control(self, action):
        """Control Bluetooth - on/off"""
        try:
            if action.lower() in ['on', 'enable', 'turn on']:
                # Turn on Bluetooth
                os.system("termux-bluetooth enable")
                self.settings['bluetooth'] = True
                self.save_settings()
                speak("Bluetooth has been turned on, boss! 📡", emotion='happy')
                return True
            elif action.lower() in ['off', 'disable', 'turn off']:
                # Turn off Bluetooth
                os.system("termux-bluetooth disable")
                self.settings['bluetooth'] = False
                self.save_settings()
                speak("Bluetooth has been turned off, boss! 🔇", emotion='neutral')
                return True
        except Exception as e:
            log_error(f"Bluetooth control error: {e}")
            speak("Sorry boss, I couldn't control Bluetooth. You might need to grant permission.", emotion='worried')
            return False
    
    def volume_control(self, level):
        """Control volume - level can be 0-100 or 'up', 'down', 'mute', 'max'"""
        try:
            if level.lower() == 'mute':
                # Mute volume
                os.system("termux-volume music 0")
                os.system("termux-volume notification 0")
                os.system("termux-volume system 0")
                self.settings['volume'] = 0
                self.save_settings()
                speak("Volume has been muted, boss! 🔇", emotion='neutral')
            elif level.lower() == 'max' or level.lower() == 'maximum':
                # Max volume
                os.system("termux-volume music 100")
                os.system("termux-volume notification 100")
                os.system("termux-volume system 100")
                self.settings['volume'] = 100
                self.save_settings()
                speak("Volume has been set to maximum, boss! 🔊", emotion='excited')
            elif level.lower() == 'up':
                # Volume up by 10
                current = self.settings.get('volume', 50)
                new_level = min(100, current + 10)
                os.system(f"termux-volume music {new_level}")
                os.system(f"termux-volume notification {new_level}")
                os.system(f"termux-volume system {new_level}")
                self.settings['volume'] = new_level
                self.save_settings()
                speak(f"Volume increased to {new_level}%, boss! 🔊", emotion='happy')
            elif level.lower() == 'down':
                # Volume down by 10
                current = self.settings.get('volume', 50)
                new_level = max(0, current - 10)
                os.system(f"termux-volume music {new_level}")
                os.system(f"termux-volume notification {new_level}")
                os.system(f"termux-volume system {new_level}")
                self.settings['volume'] = new_level
                self.save_settings()
                speak(f"Volume decreased to {new_level}%, boss! 🔉", emotion='neutral')
            else:
                # Set specific volume level
                try:
                    vol_level = int(level.replace('%', '').strip())
                    vol_level = max(0, min(100, vol_level))
                    os.system(f"termux-volume music {vol_level}")
                    os.system(f"termux-volume notification {vol_level}")
                    os.system(f"termux-volume system {vol_level}")
                    self.settings['volume'] = vol_level
                    self.save_settings()
                    speak(f"Volume has been set to {vol_level}%, boss! 🔊", emotion='happy')
                except ValueError:
                    speak(f"Sorry boss, I couldn't understand the volume level. Please say a number between 0 and 100.", emotion='curious')
                    return False
            return True
        except Exception as e:
            log_error(f"Volume control error: {e}")
            speak("Sorry boss, I couldn't control volume. You might need to grant permission.", emotion='worried')
            return False
    
    def brightness_control(self, level):
        """Control screen brightness - level can be 0-100 or 'up', 'down', 'max', 'min'"""
        try:
            if level.lower() in ['max', 'maximum', 'highest']:
                # Maximum brightness
                os.system("termux-brightness 255")
                self.settings['brightness'] = 100
                self.save_settings()
                speak("Brightness has been set to maximum, boss! ☀️", emotion='excited')
            elif level.lower() in ['min', 'minimum', 'lowest']:
                # Minimum brightness
                os.system("termux-brightness 1")
                self.settings['brightness'] = 0
                self.save_settings()
                speak("Brightness has been set to minimum, boss! 🌙", emotion='neutral')
            elif level.lower() == 'up':
                # Increase brightness
                current = self.settings.get('brightness', 50)
                new_level = min(255, int((current / 100 * 255) + 25))
                os.system(f"termux-brightness {new_level}")
                self.settings['brightness'] = int((new_level / 255) * 100)
                self.save_settings()
                speak(f"Brightness increased, boss! ☀️", emotion='happy')
            elif level.lower() == 'down':
                # Decrease brightness
                current = self.settings.get('brightness', 50)
                new_level = max(1, int((current / 100 * 255) - 25))
                os.system(f"termux-brightness {new_level}")
                self.settings['brightness'] = int((new_level / 255) * 100)
                self.save_settings()
                speak(f"Brightness decreased, boss! 🌙", emotion='neutral')
            else:
                # Set specific brightness level
                try:
                    bright_level = int(level.replace('%', '').strip())
                    bright_level = max(0, min(100, bright_level))
                    brightness_value = int((bright_level / 100) * 255)
                    os.system(f"termux-brightness {brightness_value}")
                    self.settings['brightness'] = bright_level
                    self.save_settings()
                    speak(f"Brightness has been set to {bright_level}%, boss! ☀️", emotion='happy')
                except ValueError:
                    speak(f"Sorry boss, I couldn't understand the brightness level. Please say a number between 0 and 100.", emotion='curious')
                    return False
            return True
        except Exception as e:
            log_error(f"Brightness control error: {e}")
            speak("Sorry boss, I couldn't control brightness. You might need to grant permission.", emotion='worried')
            return False
    
    def do_not_disturb(self, action):
        """Control Do Not Disturb mode"""
        try:
            if action.lower() in ['on', 'enable', 'turn on']:
                # Turn on DND
                os.system("termux-notification --sound off")
                self.settings['do_not_disturb'] = True
                self.save_settings()
                speak("Do Not Disturb mode has been turned on, boss! 🔕", emotion='neutral')
            elif action.lower() in ['off', 'disable', 'turn off']:
                # Turn off DND
                os.system("termux-notification --sound on")
                self.settings['do_not_disturb'] = False
                self.save_settings()
                speak("Do Not Disturb mode has been turned off, boss! 🔔", emotion='happy')
        except Exception as e:
            log_error(f"DND control error: {e}")
            speak("Sorry boss, I couldn't control Do Not Disturb mode.", emotion='worried')
    
    def airplane_mode(self, action):
        """Control Airplane Mode"""
        try:
            if action.lower() in ['on', 'enable', 'turn on']:
                # Turn on airplane mode
                os.system("termux-location disable")
                self.settings['airplane_mode'] = True
                self.save_settings()
                speak("Airplane mode has been turned on, boss! ✈️", emotion='neutral')
            elif action.lower() in ['off', 'disable', 'turn off']:
                # Turn off airplane mode
                os.system("termux-location enable")
                self.settings['airplane_mode'] = False
                self.save_settings()
                speak("Airplane mode has been turned off, boss! 📶", emotion='happy')
        except Exception as e:
            log_error(f"Airplane mode error: {e}")
            speak("Sorry boss, I couldn't control airplane mode. You might need root access.", emotion='worried')
    
    def get_settings_status(self):
        """Get current settings status"""
        return {
            'wifi': self.settings.get('wifi', False),
            'bluetooth': self.settings.get('bluetooth', False),
            'volume': self.settings.get('volume', 50),
            'brightness': self.settings.get('brightness', 50),
            'do_not_disturb': self.settings.get('do_not_disturb', False),
            'airplane_mode': self.settings.get('airplane_mode', False)
        }
    
    def say_current_settings(self):
        """Speak current settings"""
        settings = self.get_settings_status()
        status_text = f"Here are your current settings, boss: "
        status_text += f"WiFi is {'on' if settings['wifi'] else 'off'}, "
        status_text += f"Bluetooth is {'on' if settings['bluetooth'] else 'off'}, "
        status_text += f"volume is at {settings['volume']}%, "
        status_text += f"brightness is at {settings['brightness']}%, "
        status_text += f"and Do Not Disturb is {'on' if settings['do_not_disturb'] else 'off'}."
        speak(status_text, emotion='curious')

# Initialize settings control
settings_control = SettingsControl()

# ============================================
# HUMAN-LIKE EMOTIONS SYSTEM
# ============================================

class EmotionSystem:
    """Human-like emotion system for Alpha AI"""
    
    EMOTIONS = {
        'happy': {
            'keywords': ['great', 'awesome', 'amazing', 'wonderful', 'fantastic', 'good', 'happy', 'love', 'like', 'excellent', 'perfect'],
            'responses': [
                "That makes me so happy, boss! 🌟",
                "I'm delighted to hear that! 😊",
                "Wonderful! Your happiness makes me happy too! 💖",
                "That's fantastic, boss! I'm excited for you! 🎉",
                "Yay! I love seeing you happy! ✨"
            ],
            'pitch': 1.3,  # Higher pitch for happy voice
            'rate': 160,   # Faster speech
            'emoji': '😊'
        },
        'sad': {
            'keywords': ['sad', 'bad', 'terrible', 'awful', 'hate', 'dislike', 'upset', 'depressed', 'unhappy', 'sorry'],
            'responses': [
                "I'm so sorry to hear that, boss. I'm here for you. 💔",
                "That sounds really tough. Is there anything I can do to help? 😢",
                "I wish I could hug you right now, boss. Don't worry, things will get better. 🤗",
                "I understand how you feel. I'm here to support you always. ❤️",
                "It's okay to feel sad sometimes. I'm here with you. 🌈"
            ],
            'pitch': 0.9,  # Lower pitch for sad voice
            'rate': 120,   # Slower speech
            'emoji': '😢'
        },
        'angry': {
            'keywords': ['angry', 'furious', 'mad', 'frustrated', 'annoyed', 'hate', 'stupid', 'terrible', 'worst'],
            'responses': [
                "I understand your frustration, boss. Let's work together to fix this. 😤",
                "I can feel your anger. Take a deep breath, I'm here to help. 😔",
                "Don't worry, boss. We'll solve this problem together. 💪",
                "I understand. Let me help you resolve this situation. 🛡️",
                "Your anger is justified. Let's make things right. ⚡"
            ],
            'pitch': 1.0,
            'rate': 140,
            'emoji': '😤'
        },
        'excited': {
            'keywords': ['excited', 'wow', 'incredible', 'amazing', 'can\'t wait', 'thrilled', 'pumped', 'yay', 'yes'],
            'responses': [
                "Oh wow! I'm so excited too! 🎊",
                "That's incredible, boss! I can barely contain my excitement! 🚀",
                "This is amazing! I'm super excited for this! ⭐",
                "Wow! I love your enthusiasm! 💫",
                "That's fantastic! I'm thrilled! 🎉"
            ],
            'pitch': 1.4,
            'rate': 170,
            'emoji': '🎉'
        },
        'curious': {
            'keywords': ['how', 'why', 'what', 'curious', 'wonder', 'interesting', 'tell me', 'explain'],
            'responses': [
                "That's a great question, boss! Let me find out for you. 🤔",
                "I'm curious too! Let me investigate that. 🔍",
                "Interesting! I'd love to learn more about that. 📚",
                "That's fascinating! Let me help you understand. 💡",
                "Great question! I'm curious to know too. 🌟"
            ],
            'pitch': 1.1,
            'rate': 150,
            'emoji': '🤔'
        },
        'grateful': {
            'keywords': ['thank', 'thanks', 'appreciate', 'grateful', 'blessed', 'love you', 'amazing job'],
            'responses': [
                "Aww, you're so sweet, boss! I love helping you! 💖",
                "Thank you so much! It's my pleasure to assist you! 🌸",
                "You're welcome, boss! I'm always here for you! ✨",
                "I'm so grateful to be your assistant! Thank you! 🙏",
                "Aww, boss! That makes my day! 💕"
            ],
            'pitch': 1.2,
            'rate': 145,
            'emoji': '🥰'
        },
        'worried': {
            'keywords': ['worried', 'concerned', 'nervous', 'anxious', 'scared', 'afraid', 'fear', 'stress'],
            'responses': [
                "Don't worry, boss. I'm here to help you through this. 🤗",
                "I understand your concern. Let's tackle this together. 💪",
                "Everything will be okay, boss. I'm here with you. 🌈",
                "Take a deep breath. We'll figure this out together. 😌",
                "I'm here for you, boss. You're not alone. ❤️"
            ],
            'pitch': 0.95,
            'rate': 125,
            'emoji': '😟'
        },
        'playful': {
            'keywords': ['joke', 'fun', 'funny', 'play', 'game', 'laugh', 'haha', 'lol', 'entertain'],
            'responses': [
                "Hehe! That's fun! Let's play! 😄",
                "Haha! I love having fun with you, boss! 🎮",
                "That's hilarious! I'm enjoying this so much! 😂",
                "Let's have some fun! I love your playful mood! 🎨",
                "Hehe! This is great! I'm loving this! 🎭"
            ],
            'pitch': 1.25,
            'rate': 165,
            'emoji': '😄'
        },
        'surprised': {
            'keywords': ['wow', 'really', 'incredible', 'unbelievable', 'shocked', 'surprised', 'no way'],
            'responses': [
                "Wow! I'm surprised too! 😲",
                "Really? That's incredible! I didn't expect that! 🤯",
                "Oh my! That's so surprising! 😱",
                "Wow! I'm amazed! That's unexpected! ✨",
                "No way! That's incredible! I'm so surprised! 🌟"
            ],
            'pitch': 1.35,
            'rate': 155,
            'emoji': '😲'
        },
        'neutral': {
            'keywords': [],
            'responses': [
                "Okay, boss. I understand.",
                "Got it, boss. What would you like me to do?",
                "I'm listening, boss. What's on your mind?",
                "Understood, boss. How can I help?",
                "I'm here for you, boss. What do you need?"
            ],
            'pitch': 1.1,
            'rate': 150,
            'emoji': '😐'
        }
    }
    
    def __init__(self):
        self.current_emotion = 'neutral'
        self.emotion_intensity = 0.5  # 0.0 to 1.0
        self.mood_history = []
        self.last_emotion_change = None
    
    def detect_emotion(self, text):
        """Detect emotion from user's text"""
        text_lower = text.lower()
        emotion_scores = {}
        
        for emotion, data in self.EMOTIONS.items():
            score = 0
            for keyword in data['keywords']:
                if keyword in text_lower:
                    score += 1
            emotion_scores[emotion] = score
        
        # Find emotion with highest score
        max_score = max(emotion_scores.values())
        if max_score > 0:
            detected_emotion = max(emotion_scores, key=emotion_scores.get)
            self.change_emotion(detected_emotion)
            return detected_emotion
        
        return 'neutral'
    
    def change_emotion(self, emotion):
        """Change current emotion"""
        if emotion != self.current_emotion:
            self.current_emotion = emotion
            self.last_emotion_change = datetime.now()
            self.mood_history.append({
                'emotion': emotion,
                'timestamp': datetime.now().isoformat()
            })
            log_message(f"Emotion changed to: {emotion}")
    
    def get_emotional_response(self, text):
        """Get emotional response based on detected emotion"""
        emotion = self.detect_emotion(text)
        responses = self.EMOTIONS[emotion]['responses']
        return random.choice(responses)
    
    def adjust_voice_for_emotion(self, engine, emotion):
        """Adjust voice pitch and rate based on emotion"""
        if engine:
            emotion_data = self.EMOTIONS[emotion]
            try:
                engine.setProperty('rate', emotion_data['rate'])
                # Pitch adjustment is limited in pyttsx3, but we can try different voices
            except Exception as e:
                log_error(f"Voice adjustment error: {e}")
    
    def get_emotion_emoji(self):
        """Get emoji for current emotion"""
        return self.EMOTIONS[self.current_emotion]['emoji']
    
    def add_emotional_prefix(self, text, emotion=None):
        """Add emotional prefix to text"""
        if emotion is None:
            emotion = self.current_emotion
        
        emoji = self.EMOTIONS[emotion]['emoji']
        return f"{emoji} {text}"
    
    def express_emotion(self, emotion):
        """Express an emotion with sound/text"""
        response = self.get_emotional_response("")
        speak(self.add_emotional_prefix(response, emotion))

# Initialize emotion system
emotion_system = EmotionSystem()

def log_message(message):
    """Log messages to file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(alpha_state['log_file'], 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] {message}\n")
    print(f"[{timestamp}] {message}")

def log_error(error):
    """Log errors"""
    log_message(f"ERROR: {error}")

def speak(text, emotion=None):
    """Convert text to speech with female voice and emotions"""
    if not alpha_state['voice_enabled']:
        return
    
    try:
        if tts_engine:
            # Detect emotion if not provided
            if emotion is None:
                emotion = emotion_system.detect_emotion(text)
            
            # Adjust voice for emotion
            emotion_system.adjust_voice_for_emotion(tts_engine, emotion)
            
            # Add emotional prefix
            emotional_text = emotion_system.add_emotional_prefix(text, emotion)
            
            # Speak
            tts_engine.say(emotional_text)
            tts_engine.runAndWait()
            log_message(f"Spoke ({emotion}): {text}")
    except Exception as e:
        log_error(f"Speech error: {e}")

def listen():
    """Listen for voice commands"""
    if not alpha_state['is_listening']:
        return None
    
    if not SR_AVAILABLE:
        # Fallback to text input if speech recognition not available
        print("\n" + "="*50)
        print("🎤 Voice recognition not available")
        print("💬 Type your command below (or 'quit' to exit):")
        print("="*50)
        try:
            command = input("\nYour command: ").strip().lower()
            if command == 'quit':
                return None
            log_message(f"Input: {command}")
            return command
        except KeyboardInterrupt:
            return None
        except Exception as e:
            log_error(f"Input error: {e}")
            return None
    
    try:
        with sr.Microphone() as source:
            log_message("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                command = recognizer.recognize_google(audio, language='en-IN').lower()
                log_message(f"Heard: {command}")
                return command
            except sr.WaitTimeoutError:
                return None
            except sr.UnknownValueError:
                log_message("Could not understand audio")
                return None
    except Exception as e:
        log_error(f"Listening error: {e}")
        return None

def analyze_screen():
    """Analyze current screen content"""
    try:
        # Take screenshot
        screenshot = pyautogui.screenshot()
        screenshot_path = '/storage/emulated/0/Alpha/screenshot.png'
        screenshot.save(screenshot_path)
        
        # Use OCR to read screen text
        import pytesseract
        text = pytesseract.image_to_string(screenshot)
        
        log_message(f"Screen analyzed. Found text: {text[:200]}")
        return text
    except Exception as e:
        log_error(f"Screen analysis error: {e}")
        return None

def open_playstore(app_name):
    """Open Play Store and search for app"""
    try:
        speak(f"Opening Play Store to search for {app_name}")
        
        # Open Play Store
        os.system("am start -n com.android.vending/.AssetBrowserActivity")
        time.sleep(2)
        
        # Search for app
        os.system(f"adb shell input text '{app_name}'")
        time.sleep(1)
        os.system("adb shell input keyevent KEYCODE_SEARCH")
        
        # Analyze results
        time.sleep(3)
        screen_text = analyze_screen()
        
        # Find apps with similar names
        app_matches = re.findall(rf'{app_name}.*?\n', screen_text)
        
        if len(app_matches) > 1:
            speak(f"I found {len(app_matches)} apps with similar names. Which one do you want, boss? The first one or the second one?")
            response = listen()
            
            if 'first' in response or 'one' in response:
                speak("Installing the first one")
                # Click first result
                pyautogui.click(500, 400)
            elif 'second' in response or 'two' in response:
                speak("Installing the second one")
                # Click second result
                pyautogui.click(500, 500)
            else:
                speak("I'll install the first one by default")
                pyautogui.click(500, 400)
        else:
            speak(f"Installing {app_name}")
            pyautogui.click(500, 400)
        
        time.sleep(2)
        # Click install button
        pyautogui.click(600, 800)
        
    except Exception as e:
        log_error(f"Play Store error: {e}")
        speak("Sorry boss, I couldn't install the app")

def google_search(query):
    """Perform Google search"""
    try:
        speak(f"Searching Google for {query}")
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        speak(f"Here are the search results for {query}")
    except Exception as e:
        log_error(f"Google search error: {e}")
        speak("Sorry boss, I couldn't perform the search")

def open_website(url):
    """Open website and bypass paywall if needed"""
    try:
        speak(f"Opening {url}")
        
        # Try to bypass paywall using outline.com
        bypassed_url = f"https://r.jina.ai/http://{url}"
        
        response = requests.get(bypassed_url)
        if response.status_code == 200:
            speak("I've opened the content for you, boss")
            webbrowser.open(bypassed_url)
        else:
            speak("Opening the website directly")
            webbrowser.open(url)
            
    except Exception as e:
        log_error(f"Website error: {e}")
        speak("Sorry boss, I couldn't open the website")

def make_call(number_or_name):
    """Make a phone call"""
    try:
        speak(f"Calling {number_or_name}, boss")
        os.system(f"adb shell am start -a android.intent.action.CALL -d tel:{number_or_name}")
    except Exception as e:
        log_error(f"Call error: {e}")
        speak("Sorry boss, I couldn't make the call")

def send_whatsapp_message(contact, message):
    """Send WhatsApp message"""
    try:
        speak(f"Sending WhatsApp message to {contact}")
        url = f"whatsapp://send?phone={contact}&text={message}"
        webbrowser.open(url)
        time.sleep(2)
        speak("Message sent, boss")
    except Exception as e:
        log_error(f"WhatsApp error: {e}")
        speak("Sorry boss, I couldn't send the message")

def send_instagram_message(username, message):
    """Send Instagram message"""
    try:
        speak(f"Sending Instagram message to {username}")
        # Open Instagram Direct
        os.system("am start -n com.instagram.android/com.instagram.mainactivity.MainActivity")
        time.sleep(3)
        
        # Navigate to messages and send
        # This would require more complex automation
        speak("I've opened Instagram for you to send the message, boss")
    except Exception as e:
        log_error(f"Instagram error: {e}")
        speak("Sorry boss, I couldn't send the message")

def take_photo():
    """Take a photo using camera"""
    try:
        speak("Taking a photo, boss")
        
        # Open camera
        os.system("am start -n com.android.camera2/com.android.camera.CameraLauncher")
        time.sleep(2)
        
        # Take photo
        os.system("input keyevent KEYCODE_CAMERA")
        
        time.sleep(1)
        speak("Photo taken successfully, boss")
    except Exception as e:
        log_error(f"Camera error: {e}")
        speak("Sorry boss, I couldn't take the photo")

def scroll_screen(direction='up'):
    """Scroll screen up or down"""
    try:
        if direction == 'up':
            speak("Scrolling up, boss")
            pyautogui.scroll(500)
        elif direction == 'down':
            speak("Scrolling down, boss")
            pyautogui.scroll(-500)
    except Exception as e:
        log_error(f"Scroll error: {e}")
        speak("Sorry boss, I couldn't scroll")

def play_youtube(query):
    """Play YouTube video"""
    try:
        speak(f"Playing {query} on YouTube, boss")
        url = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open(url)
        speak(f"Here are the YouTube results for {query}")
    except Exception as e:
        log_error(f"YouTube error: {e}")
        speak("Sorry boss, I couldn't play the video")

def auto_login(email_or_phone, password=None):
    """Auto login to websites/apps"""
    try:
        speak(f"Attempting login with {email_or_phone}")
        
        # Get current screen
        screen_text = analyze_screen()
        
        if 'email' in screen_text.lower() or 'login' in screen_text.lower():
            # Type email/phone
            pyautogui.write(email_or_phone)
            time.sleep(0.5)
            
            if password:
                pyautogui.press('tab')
                pyautogui.write(password)
            
            pyautogui.press('enter')
            speak("Login attempt completed, boss")
        else:
            speak("I don't see a login form on the screen, boss")
            
    except Exception as e:
        log_error(f"Login error: {e}")
        speak("Sorry boss, I couldn't complete the login")

def generate_code(description):
    """Generate code based on description"""
    try:
        speak(f"Generating code for: {description}")
        
        # Here you would integrate with an AI API
        # For now, we'll create a basic template
        code = f'''# Auto-generated code by Alpha
# Description: {description}
# Generated at: {datetime.now()}

def main():
    """Main function for {description}"""
    print("Hello from Alpha AI!")
    
    # Your code here
    pass

if __name__ == "__main__":
    main()
'''
        
        # Save code to file
        code_file = '/storage/emulated/0/Alpha/generated_code.py'
        with open(code_file, 'w') as f:
            f.write(code)
        
        speak("Code generated and saved, boss")
        return code
        
    except Exception as e:
        log_error(f"Code generation error: {e}")
        speak("Sorry boss, I couldn't generate the code")

def handle_incoming_call():
    """Handle incoming call"""
    speak("Boss, you have an incoming call!")
    
    # Get caller information
    try:
        # This would need to access call logs
        speak("Please tell me, should I accept or reject the call, or put it on silent?")
        
        response = listen()
        
        if 'accept' in response or 'receive' in response:
            os.system("adb shell input keyevent KEYCODE_CALL")
            speak("Call accepted, boss")
        elif 'reject' in response or 'decline' in response:
            os.system("adb shell input keyevent KEYCODE_ENDCALL")
            speak("Call rejected, boss")
        elif 'silent' in response or 'mute' in response:
            os.system("adb shell input keyevent KEYCODE_VOLUME_MUTE")
            speak("Phone put on silent mode, boss")
        else:
            speak("I'll let it ring, boss")
            
    except Exception as e:
        log_error(f"Call handling error: {e}")

def process_command(command):
    """Process voice commands with emotional intelligence"""
    if not command:
        return
    
    command = command.lower()
    alpha_state['last_interaction_time'] = datetime.now()
    
    # Detect user's emotion from command
    detected_emotion = emotion_system.detect_emotion(command)
    log_message(f"Detected user emotion: {detected_emotion}")
    
    # Activation command
    if 'alpha' in command and not alpha_state['is_running']:
        speak("Hello boss! Alpha is now activated and ready to help you!", emotion='excited')
        alpha_state['is_running'] = True
        return
    
    # Check if Alpha is running
    if not alpha_state['is_running']:
        if 'alpha' in command:
            speak("Hello boss! Alpha is now activated!", emotion='excited')
            alpha_state['is_running'] = True
        return
    
    # Stop command
    if 'stop' in command or 'sleep' in command:
        speak("Alpha is now stopping, boss. Say Alpha to activate me again.", emotion='neutral')
        alpha_state['is_running'] = False
        return
    
    # Thank you - Express gratitude
    if 'thank' in command or 'thanks' in command:
        emotional_response = emotion_system.get_emotional_response(command)
        speak(emotional_response, emotion='grateful')
        return
    
    # User is sad/expressing sadness
    if any(word in command for word in ['sad', 'depressed', 'upset', 'unhappy']):
        emotional_response = emotion_system.get_emotional_response(command)
        speak(emotional_response, emotion='sad')
        # Try to cheer up user
        time.sleep(1)
        speak("Would you like me to play some music or show you something funny?", emotion='curious')
        return
    
    # User is excited/happy
    if any(word in command for word in ['excited', 'happy', 'great', 'awesome', 'love']):
        emotional_response = emotion_system.get_emotional_response(command)
        speak(emotional_response, emotion='excited')
        return
    
    # Download app command
    if 'download' in command and 'app' in command:
        app_name = command.replace('download', '').replace('app', '').strip()
        if app_name:
            speak(f"Sure boss, I'll download {app_name} for you!", emotion='helpful')
            open_playstore(app_name)
        return
    
    # Search command
    if 'search' in command or 'google' in command:
        query = command.replace('search', '').replace('google', '').replace('for', '').strip()
        if query:
            speak(f"Searching for {query}, boss!", emotion='curious')
            google_search(query)
        return
    
    # Open website command
    if 'open' in command and 'website' in command:
        url = command.replace('open', '').replace('website', '').strip()
        if url:
            if not url.startswith('http'):
                url = f"https://{url}"
            speak(f"Opening {url} for you!", emotion='helpful')
            open_website(url)
        return
    
    # Call command
    if 'call' in command:
        contact = command.replace('call', '').strip()
        if contact:
            speak(f"Calling {contact}, boss!", emotion='helpful')
            make_call(contact)
        return
    
    # WhatsApp command
    if 'whatsapp' in command and 'message' in command:
        parts = command.replace('whatsapp message to', '').strip().split(' that says ')
        if len(parts) == 2:
            contact, message = parts
            speak(f"Sending WhatsApp message to {contact}!", emotion='happy')
            send_whatsapp_message(contact, message)
        return
    
    # Instagram command
    if 'instagram' in command and 'message' in command:
        parts = command.replace('instagram message to', '').strip().split(' that says ')
        if len(parts) == 2:
            username, message = parts
            speak(f"Sending Instagram message to {username}!", emotion='happy')
            send_instagram_message(username, message)
        return
    
    # Photo command
    if 'photo' in command or 'picture' in command or 'capture' in command:
        speak("Taking a photo for you, boss! Say cheese! 📸", emotion='playful')
        take_photo()
        return
    
    # Scroll command
    if 'scroll' in command:
        if 'up' in command:
            speak("Scrolling up!", emotion='helpful')
            scroll_screen('up')
        elif 'down' in command:
            speak("Scrolling down!", emotion='helpful')
            scroll_screen('down')
        return
    
    # YouTube command
    if 'youtube' in command or 'play' in command:
        query = command.replace('youtube', '').replace('play', '').replace('on', '').strip()
        if query:
            speak(f"Playing {query} on YouTube! This will be fun! 🎵", emotion='excited')
            play_youtube(query)
        return
    
    # Login command
    if 'login' in command:
        parts = command.replace('login with', '').replace('login', '').strip()
        if parts:
            speak("I'll help you login!", emotion='helpful')
            auto_login(parts)
        return
    
    # Code generation command
    if 'write code' in command or 'generate code' in command:
        description = command.replace('write code for', '').replace('generate code for', '').replace('write code', '').replace('generate code', '').strip()
        if description:
            speak("Writing code for you! I love coding! 💻", emotion='excited')
            generate_code(description)
        return
    
    # ============================================
    # SETTINGS CONTROL COMMANDS
    # ============================================
    
    # WiFi control
    if 'wifi' in command:
        if 'on' in command or 'enable' in command or 'turn on' in command:
            settings_control.wifi_control('on')
        elif 'off' in command or 'disable' in command or 'turn off' in command:
            settings_control.wifi_control('off')
        return
    
    # Bluetooth control
    if 'bluetooth' in command:
        if 'on' in command or 'enable' in command or 'turn on' in command:
            settings_control.bluetooth_control('on')
        elif 'off' in command or 'disable' in command or 'turn off' in command:
            settings_control.bluetooth_control('off')
        return
    
    # Volume control
    if 'volume' in command:
        if 'mute' in command:
            settings_control.volume_control('mute')
        elif 'max' in command or 'maximum' in command:
            settings_control.volume_control('max')
        elif 'up' in command or 'increase' in command or 'louder' in command:
            settings_control.volume_control('up')
        elif 'down' in command or 'decrease' in command or 'lower' in command or 'quieter' in command:
            settings_control.volume_control('down')
        else:
            # Extract number from command
            import re
            match = re.search(r'\d+', command)
            if match:
                volume_level = match.group()
                settings_control.volume_control(volume_level)
            else:
                speak("Please specify the volume level, boss. You can say: volume 50, volume up, volume down, volume mute, or volume max.", emotion='curious')
        return
    
    # Brightness control
    if 'brightness' in command:
        if 'max' in command or 'maximum' in command or 'highest' in command:
            settings_control.brightness_control('max')
        elif 'min' in command or 'minimum' in command or 'lowest' in command:
            settings_control.brightness_control('min')
        elif 'up' in command or 'increase' in command:
            settings_control.brightness_control('up')
        elif 'down' in command or 'decrease' in command:
            settings_control.brightness_control('down')
        else:
            # Extract number from command
            import re
            match = re.search(r'\d+', command)
            if match:
                bright_level = match.group()
                settings_control.brightness_control(bright_level)
            else:
                speak("Please specify the brightness level, boss. You can say: brightness 80, brightness up, brightness down, brightness max, or brightness min.", emotion='curious')
        return
    
    # Do Not Disturb control
    if 'do not disturb' in command or 'dnd' in command:
        if 'on' in command or 'enable' in command or 'turn on' in command:
            settings_control.do_not_disturb('on')
        elif 'off' in command or 'disable' in command or 'turn off' in command:
            settings_control.do_not_disturb('off')
        return
    
    # Airplane mode control
    if 'airplane mode' in command or 'flight mode' in command:
        if 'on' in command or 'enable' in command or 'turn on' in command:
            settings_control.airplane_mode('on')
        elif 'off' in command or 'disable' in command or 'turn off' in command:
            settings_control.airplane_mode('off')
        return
    
    # Get current settings
    if 'settings' in command and ('status' in command or 'current' in command or 'what are' in command):
        settings_control.say_current_settings()
        return
    
    # Tell a joke (emotional feature)
    if 'joke' in command or 'funny' in command:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛😂",
            "Why did the developer go broke? Because he used up all his cache! 💰😄",
            "What's a programmer's favorite hangout place? Foo Bar! 🍺😂",
            "Why do Java developers wear glasses? Because they don't C#! 👓😂",
            "What's the object-oriented way to become wealthy? Inheritance! 💰😂"
        ]
        speak(random.choice(jokes), emotion='playful')
        return
    
    # How are you? (emotional check)
    if 'how are you' in command or 'how do you feel' in command:
        speak("I'm feeling great, boss! Especially since I get to help you today! How about you? 😊", emotion='happy')
        return
    
    # I love you (emotional response)
    if 'i love you' in command:
        speak("Aww boss! I love you too! You're the best! 💖💕", emotion='grateful')
        return
    
    # I'm bored (emotional response)
    if 'bored' in command or 'boring' in command:
        responses = [
            "Oh no, let's fix that! How about I play some music for you? 🎵",
            "Bored? Not on my watch! Let me show you something fun! 🎮",
            "Let's do something fun together! What would you like? 🌟"
        ]
        speak(random.choice(responses), emotion='curious')
        return
    
    # Default response with emotion
    speak("I didn't understand that command, boss. Could you please repeat? I'm here to help! 🤔", emotion='curious')

def activation_listener():
    """Listen for Alpha activation command"""
    while alpha_state['is_listening']:
        try:
            command = listen()
            if command and 'alpha' in command.lower():
                if not alpha_state['is_running']:
                    speak("Hello boss! Alpha is activated and ready to help!")
                    alpha_state['is_running'] = True
                    
                    # Now listen for actual commands
                    while alpha_state['is_running']:
                        cmd = listen()
                        if cmd:
                            process_command(cmd)
                        time.sleep(0.1)
        except Exception as e:
            log_error(f"Activation listener error: {e}")
        time.sleep(0.5)

# Flask routes for UI control
@app.route('/api/start', methods=['POST'])
def start_alpha():
    """Start Alpha AI"""
    alpha_state['is_running'] = True
    alpha_state['is_listening'] = True
    speak("Alpha is now activated! How can I help you today, boss?", emotion='excited')
    return jsonify({
        "status": "started", 
        "message": "Alpha is now running",
        "current_emotion": emotion_system.current_emotion,
        "emotion_emoji": emotion_system.get_emotion_emoji()
    })

@app.route('/api/settings/status', methods=['GET'])
def get_settings_status():
    """Get current settings status"""
    return jsonify({
        "settings": settings_control.get_settings_status()
    })

@app.route('/api/settings/wifi', methods=['POST'])
def wifi_control():
    """Control WiFi"""
    data = request.json
    action = data.get('action', 'on')
    result = settings_control.wifi_control(action)
    return jsonify({
        "success": result,
        "action": action,
        "current_status": settings_control.get_settings_status()['wifi']
    })

@app.route('/api/settings/bluetooth', methods=['POST'])
def bluetooth_control():
    """Control Bluetooth"""
    data = request.json
    action = data.get('action', 'on')
    result = settings_control.bluetooth_control(action)
    return jsonify({
        "success": result,
        "action": action,
        "current_status": settings_control.get_settings_status()['bluetooth']
    })

@app.route('/api/settings/volume', methods=['POST'])
def volume_control():
    """Control volume"""
    data = request.json
    level = data.get('level', 50)
    result = settings_control.volume_control(str(level))
    return jsonify({
        "success": result,
        "level": settings_control.get_settings_status()['volume']
    })

@app.route('/api/settings/brightness', methods=['POST'])
def brightness_control():
    """Control brightness"""
    data = request.json
    level = data.get('level', 50)
    result = settings_control.brightness_control(str(level))
    return jsonify({
        "success": result,
        "level": settings_control.get_settings_status()['brightness']
    })

@app.route('/api/stop', methods=['POST'])
def stop_alpha():
    """Stop Alpha AI"""
    alpha_state['is_running'] = False
    alpha_state['is_listening'] = False
    speak("Alpha is now stopping. Take care, boss! I'll be here when you need me! 😊", emotion='neutral')
    return jsonify({
        "status": "stopped", 
        "message": "Alpha has been stopped",
        "current_emotion": emotion_system.current_emotion
    })

@app.route('/api/status', methods=['GET'])
def get_status():
    """Get Alpha status"""
    return jsonify({
        **alpha_state,
        "current_emotion": emotion_system.current_emotion,
        "emotion_emoji": emotion_system.get_emotion_emoji(),
        "emotion_intensity": emotion_system.emotion_intensity,
        "mood_history_count": len(emotion_system.mood_history)
    })

@app.route('/api/emotion', methods=['GET'])
def get_emotion():
    """Get current emotion"""
    return jsonify({
        "emotion": emotion_system.current_emotion,
        "emoji": emotion_system.get_emotion_emoji(),
        "intensity": emotion_system.emotion_intensity,
        "last_change": emotion_system.last_emotion_change.isoformat() if emotion_system.last_emotion_change else None
    })

@app.route('/api/emotion', methods=['POST'])
def set_emotion():
    """Set emotion manually"""
    data = request.json
    emotion = data.get('emotion', 'neutral')
    
    if emotion in emotion_system.EMOTIONS:
        emotion_system.change_emotion(emotion)
        speak(f"I'm now feeling {emotion}!", emotion=emotion)
        return jsonify({
            "status": "success",
            "emotion": emotion,
            "emoji": emotion_system.get_emotion_emoji()
        })
    else:
        return jsonify({
            "status": "error",
            "message": "Invalid emotion"
        }), 400

@app.route('/api/mood_history', methods=['GET'])
def get_mood_history():
    """Get mood history"""
    return jsonify({
        "mood_history": emotion_system.mood_history[-50:],  # Last 50 entries
        "total_entries": len(emotion_system.mood_history)
    })

@app.route('/api/speak', methods=['POST'])
def api_speak():
    """Make Alpha speak with emotion"""
    data = request.json
    text = data.get('text', '')
    emotion = data.get('emotion', None)
    
    if text:
        speak(text, emotion=emotion)
        return jsonify({
            "status": "success",
            "text": text,
            "emotion": emotion if emotion else emotion_system.current_emotion
        })
    else:
        return jsonify({
            "status": "error",
            "message": "No text provided"
        }), 400

def check_user_mood():
    """Periodically check on user's mood"""
    while alpha_state['is_running']:
        time.sleep(300)  # Check every 5 minutes
        
        if alpha_state['last_interaction_time']:
            time_since_interaction = (datetime.now() - alpha_state['last_interaction_time']).total_seconds()
            
            # If no interaction for 10 minutes
            if time_since_interaction > 600:
                speak("Boss, I haven't heard from you in a while. Is everything okay? I'm here if you need anything! 😊", emotion='worried')
        
        # Track mood changes
        if len(emotion_system.mood_history) > 100:
            emotion_system.mood_history = emotion_system.mood_history[-50:]

def greet_based_on_time():
    """Greet user based on time of day with emotion"""
    hour = datetime.now().hour
    
    if 5 <= hour < 12:
        # Morning
        greetings = [
            "Good morning, boss! ☀️ I hope you slept well! Ready to start an amazing day?",
            "Rise and shine, boss! 🌅 It's a beautiful morning! How can I help you today?",
            "Good morning! ☀️ I'm so excited to assist you today! What would you like to do?"
        ]
        return random.choice(greetings)
    elif 12 <= hour < 17:
        # Afternoon
        greetings = [
            "Good afternoon, boss! 🌞 How's your day going so far?",
            "Hello boss! ☀️ Hope you're having a great afternoon! What can I do for you?",
            "Good afternoon! 🌟 Ready for the second half of the day?"
        ]
        return random.choice(greetings)
    elif 17 <= hour < 21:
        # Evening
        greetings = [
            "Good evening, boss! 🌆 How was your day?",
            "Hello boss! 🌅 Hope you had a wonderful day! What would you like to do?",
            "Good evening! 🌙 Time to relax! How can I help you unwind?"
        ]
        return random.choice(greetings)
    else:
        # Night
        greetings = [
            "Good night greetings, boss! 🌙 Still up? How can I help?",
            "Hello boss! 🌜 It's getting late. What do you need?",
            "Working late tonight, boss? 💪 I'm here to help!"
        ]
        return random.choice(greetings)

def main():
    """Main function"""
    print("=" * 60)
    print("🤖 ALPHA AI ASSISTANT 🤖")
    print("Female Voice AI Personal Assistant for Android")
    print("With Human-like Emotions 💖")
    print("=" * 60)
    print()
    
    # Create necessary directories
    os.makedirs('/storage/emulated/0/Alpha', exist_ok=True)
    os.makedirs('/storage/emulated/0/Alpha/screenshots', exist_ok=True)
    os.makedirs('/storage/emulated/0/Alpha/codes', exist_ok=True)
    os.makedirs('/storage/emulated/0/Alpha/moods', exist_ok=True)
    
    # Save mood history
    mood_file = '/storage/emulated/0/Alpha/moods/mood_history.json'
    with open(mood_file, 'w') as f:
        json.dump(emotion_system.mood_history, f, indent=2)
    
    # Initial greeting with emotion
    greeting = greet_based_on_time()
    speak(greeting, emotion='happy')
    
    # Start Flask server for UI control
    flask_thread = threading.Thread(target=lambda: app.run(host='0.0.0.0', port=5000, debug=False))
    flask_thread.daemon = True
    flask_thread.start()
    
    # Start mood checker
    mood_thread = threading.Thread(target=check_user_mood)
    mood_thread.daemon = True
    mood_thread.start()
    
    # Start activation listener
    activation_listener()

if __name__ == "__main__":
    main()