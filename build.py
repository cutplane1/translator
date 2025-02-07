UI_FILE = "window.ui" 
GEN_FILE = "window_generated.py"

import subprocess
import os, sys


def build_ui():
    result = subprocess.run(["pyside6-uic", UI_FILE], capture_output=True, text=True, check=True)
    with open(GEN_FILE, "w", encoding="utf-8") as output_file:
        output_file.write(result.stdout)
    print(f"{UI_FILE} -> {GEN_FILE}")

def build_exe():
    os.system("python -m nuitka --onefile main.py --enable-plugin=pyside6 --windows-console-mode=disable --output-dir=dist")

try:
    if sys.argv[1] == "ui":
        build_ui()
    elif sys.argv[1] == "exe":
        build_exe()
    elif sys.argv[1] == "all":
        build_ui()
        build_exe()
    else:
        print("Usage: python build.py [ui|exe|all]")
except IndexError:
    print("Usage: python build.py [ui|exe|all]")