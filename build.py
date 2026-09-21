import os
from pathlib import Path
import PyInstaller.__main__

dist = Path(__file__).parent / "dist"
dist.mkdir(exist_ok=True)

PyInstaller.__main__.run([
    "main.py",
    "--name=UniversalProxy",
    "--onefile",
    "--windowed",
    "--distpath", str(dist),
    "--workpath", str(Path(__file__).parent / "build"),
    "--specpath", str(Path(__file__).parent),
    "--clean",
    "--noconfirm",
    "--add-data", f"icon.png{';' if os.name == 'nt' else ':'}.",
])