import random
import os
import glob
import sys
import threading
import keyboard
import winsound
import pystray
from PIL import Image, ImageDraw

if getattr(sys, 'frozen', False):
    base_dir = os.path.join(sys._MEIPASS, "ShotgunSoundboard")
else:
    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ShotgunSoundboard")

sounds = sorted(glob.glob(os.path.join(base_dir, "*.wav")))

if not sounds:
    print("Error: No valid sound files found!")
    sys.exit(1)

running = True
playing_lock = threading.Lock()

def play_random_shotgun(e):
    if not (sounds and running):
        return
    if not playing_lock.acquire(blocking=False):
        return
    sound = random.choice(sounds)
    def _play():
        try:
            winsound.PlaySound(sound, winsound.SND_FILENAME)
        finally:
            playing_lock.release()
    threading.Thread(target=_play, daemon=True).start()

def create_icon():
    img = Image.new('RGB', (64, 64), color='black')
    draw = ImageDraw.Draw(img)
    draw.rectangle([16, 16, 48, 48], fill='red')
    try:
        draw.text((20, 20), "🔫", fill='white')
    except:
        draw.text((22, 22), "SG", fill='white')
    return img

def on_quit(icon, item):
    global running
    running = False
    icon.stop()
    keyboard.unhook_all()
    sys.exit(0)

def on_about(icon, item):
    print("Shotgun Keyboard - Press any key for shotgun sounds")

keyboard.on_press(play_random_shotgun)

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
print("Right-click tray icon > Quit to exit.")
icon.run()