import random
import os
import keyboard
import winsound

sound_folder = r"D:\ShotgunKeyboard\Shotgun_keyboard\ShotgunSoundboard"
sound_files = ["Shotgun_1.wav", "Shotgun_2.wav", "Shotgun_3.wav", "Shotgun_4.wav"]

sounds = []
for file in sound_files:
    path = os.path.join(sound_folder, file)
    if os.path.exists(path):
        sounds.append(path)
    else:
        print(f"Warning: Could not find {file}")

if not sounds:
    print("Error: No valid sound files found!")
else:
    print("Shotgun soundboard is running! Press any key (Press ESC to quit)...\n")

def play_random_shotgun(e):
    if sounds:
        random_sound = random.choice(sounds)
        winsound.PlaySound(random_sound, winsound.SND_ASYNC | winsound.SND_FILENAME)

keyboard.on_press(play_random_shotgun)
keyboard.wait('esc')