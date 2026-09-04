import os
import random
import subprocess
import sys
from pathlib import Path
from pynput import keyboard

if getattr(sys, 'frozen', False):
    BASE_DIR = Path(sys._MEIPASS)
else:
    BASE_DIR = Path(__file__).parent

SOUNDS_DIR = BASE_DIR / "Sounds"
SOUND_FILES = list(SOUNDS_DIR.glob("*.mp3"))

if not SOUND_FILES:
    print("No sound files found in Sounds/ directory")
    sys.exit(1)

print(f"Found {len(SOUND_FILES)} sound files")
print("Press any key to play a random shotgun sound...")
print("Press ESC to exit")

def play_random_sound():
    sound_file = random.choice(SOUND_FILES)
    try:
        subprocess.run(
            ["powershell", "-c", f"Add-Type -AssemblyName PresentationCore; \$player = New-Object System.Windows.Media.MediaPlayer; \$player.Open('{sound_file}'); \$player.Play(); Start-Sleep -m 100"],
            capture_output=True,
            check=False
        )
    except Exception as e:
        print(f"Error playing sound: {e}")

def on_press(key):
    play_random_sound()

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()