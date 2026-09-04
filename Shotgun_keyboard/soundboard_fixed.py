import random
import os
import glob
import sys
import queue
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

MODE_INTERRUPT = "Interrupt"
MODE_QUEUE = "Queue"
MODE_DISCARD = "Discard"

running = True
mode = MODE_DISCARD

play_lock = threading.Lock()
sound_queue = queue.Queue()


def set_mode(new_mode):
    global mode
    mode = new_mode
    if new_mode != MODE_QUEUE:
        while True:
            try:
                sound_queue.get_nowait()
            except queue.Empty:
                break


def play_random_shotgun(e):
    if not (sounds and running):
        return
    path = random.choice(sounds)
    m = mode
    if m == MODE_INTERRUPT:
        winsound.PlaySound(path, winsound.SND_ASYNC | winsound.SND_FILENAME)
    elif m == MODE_DISCARD:
        if play_lock.acquire(blocking=False):
            def _play():
                try:
                    winsound.PlaySound(path, winsound.SND_FILENAME)
                finally:
                    play_lock.release()
            threading.Thread(target=_play, daemon=True).start()
    elif m == MODE_QUEUE:
        sound_queue.put(path)


def _queue_worker():
    while True:
        path = sound_queue.get()
        if not running or path is None:
            break
        winsound.PlaySound(path, winsound.SND_FILENAME)


def create_icon():
    img = Image.new('RGB', (64, 64), color='black')
    draw = ImageDraw.Draw(img)
    draw.rectangle([16, 16, 48, 48], fill='red')
    try:
        draw.text((20, 20), "\U0001F52B", fill='white')
    except Exception:
        draw.text((22, 22), "SG", fill='white')
    return img


def on_quit(icon, item):
    global running
    running = False
    sound_queue.put_nowait(None)
    icon.stop()
    keyboard.unhook_all()
    sys.exit(0)


def on_about(icon, item):
    print("Shotgun Keyboard - Press any key for shotgun sounds")


threading.Thread(target=_queue_worker, daemon=True).start()
keyboard.on_press(play_random_shotgun)

icon = pystray.Icon(
    "ShotgunKeyboard",
    create_icon(),
    menu=pystray.Menu(
        pystray.MenuItem("Playback Mode", pystray.Menu(
            pystray.MenuItem(
                MODE_INTERRUPT,
                lambda icon, item: set_mode(MODE_INTERRUPT),
                radio=True,
                checked=lambda item: mode == MODE_INTERRUPT,
            ),
            pystray.MenuItem(
                MODE_QUEUE,
                lambda icon, item: set_mode(MODE_QUEUE),
                radio=True,
                checked=lambda item: mode == MODE_QUEUE,
            ),
            pystray.MenuItem(
                MODE_DISCARD,
                lambda icon, item: set_mode(MODE_DISCARD),
                radio=True,
                checked=lambda item: mode == MODE_DISCARD,
            ),
        )),
        pystray.MenuItem("About", on_about),
        pystray.MenuItem("Quit", on_quit),
    ),
    title="Shotgun Keyboard - Running",
)

print("Shotgun Keyboard running in tray. Press any key for sounds.")
print("Right-click tray icon > Playback Mode to choose: Interrupt / Queue / Discard.")
icon.run()