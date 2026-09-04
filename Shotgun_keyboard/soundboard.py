import random
import os
import pygame
import keyboard

# Initialize the pygame mixer for audio
pygame.mixer.init()

# Path to your sound folder (current directory)
sound_folder = os.path.dirname(os.path.abspath(__file__))

# Load the 4 shotgun sounds into a list
sound_files = ["shotgun1.wav", "shotgun2.wav", "shotgun3.wav", "shotgun4.wav"]
sounds = []

for file in sound_files:
    path = os.path.join(sound_folder, file)
    if os.path.exists(path):
        sounds.append(pygame.mixer.Sound(path))
    else:
        print(f"Warning: Could not find {file} in the directory.")

if not sounds:
    print("Error: No valid sound files loaded! Check your filenames.")
else:
    print("Shotgun soundboard is running! Press any key (Press ESC to quit)...\n")

def play_random_shotgun(e):
    # Pick and play a random sound from the loaded list
    if sounds:
        random_sound = random.choice(sounds)
        random_sound.play()

# Hook into every key event globally
keyboard.on_press(play_random_shotgun)

# Keep the script running until you press Escape to exit cleanly
keyboard.wait('esc')