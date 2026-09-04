# Shotgun Keyboard

A fun Windows tray application that plays a random shotgun sound every time you press any key on your keyboard.

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)

## Features

- Plays a random shotgun blast from a library of 13 sounds on every keypress
- Runs silently in the system tray (bottom-right corner)
- Fully self-contained portable `.exe` — no Python or dependencies required
- Auto-elevates to Administrator on launch for global keyboard hook
- **ESC** plays a sound like any other key (does not quit)
- Right-click the tray icon → **Quit** to exit

## Usage

### Portable executable (recommended)

Build with PyInstaller:

```bash
pyinstaller --onefile --uac-admin --add-data "Shotgun_keyboard/ShotgunSoundboard;ShotgunSoundboard" --name ShotgunKeyboardPortable Shotgun_keyboard/soundboard_fixed.py
```

Then run `dist/ShotgunKeyboardPortable.exe`:

1. Double-click the `.exe` and accept the UAC prompt
2. Press any key — enjoy the shotguns
3. Right-click the tray icon → **Quit** to exit

Share the single `.exe` with anyone; it runs standalone on any Windows 10/11 machine.

### From source

Requirements: Python 3.10+, `pystray`, `pillow`, `keyboard`.

```bash
pip install pystray pillow keyboard
python Shotgun_keyboard/soundboard_fixed.py
```

## Sound library

Sounds live in `Shotgun_keyboard/ShotgunSoundboard/`. Drop any `.wav` file into
that folder and rebuild the `.exe` to include it — the script loads every
`.wav` it finds automatically.

## Project layout

```
├── Shotgun_keyboard/
│   ├── soundboard_fixed.py      # Main app (tray + winsound, no pygame)
│   └── ShotgunSoundboard/       # 13 shotgun .wav files
├── README.md
├── LICENSE
└── .gitignore
```

## Notes

- Global keyboard hooks on Windows require Administrator privileges; the app
  handles this automatically via its UAC manifest.
- `build/`, `dist/`, and `*.spec` are git-ignored build artifacts.

## License

[MIT](LICENSE)