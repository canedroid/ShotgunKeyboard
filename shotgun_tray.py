import os
import random
import subprocess
import sys
import threading
from pathlib import Path
from pynput import keyboard
import pystray
from PIL import Image, ImageDraw

if getattr(sys, 'frozen', False):
    BASE_DIR = Path(sys._MEIPASS)
else:
    BASE_DIR = Path(__file__).parent

SOUNDS_DIR = BASE_DIR / "Sounds"
SOUND_FILES = list(SOUNDS_DIR.glob("*.mp3"))

if not SOUND_FILES:
    print("No sound files found in Sounds/ directory")
    sys.exit(1)

running = True

def play_random_sound():
    sound_file = random.choice(SOUND_FILES)
    try:
        subprocess.run(
            ["powershell", "-c", f"Add-Type -AssemblyName PresentationCore; $player = New-Object System.Windows.Media.MediaPlayer; $player.Open('{sound_file}'); $player.Play(); Start-Sleep -m 100"],
            capture_output=True,
            check=False
        )
    except Exception as e:
        print(f"Error playing sound: {e}")

def on_press(key):
    if running:
        play_random_sound()

def on_release(key):
    pass

def create_icon():
    img = Image.new('RGB', (64, 64), color='black')
    draw = ImageDraw.Draw(img)
    draw.rectangle([16, 16, 48, 48], fill='red')
    draw.text((20, 20), "🔫", fill='white')
    return img

def on_quit(icon, item):
    global running
    running = False
    icon.stop()
    listener.stop()
    sys.exit(0)

def on_about(icon, item):
    print("Shotgun Keyboard - Press any key for shotgun sounds")

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

icon = pystray.Icon(
    "ShotgunKeyboard",
    create_icon(),
    menu=pystray.Menu(
        pystray.MenuItem("About", on_about),
        pystray.MenuItem("Quit", on_quit)
    ),
    title="Shotgun Keyboard - Running"
)

print("Shotgun Keyboard running in tray. Press any key for sounds.")
print("Right-click tray icon to quit.")
icon.run()