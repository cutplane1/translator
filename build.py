UI_FILE = "window.ui" 
GEN_FILE = "window_generated.py"


import subprocess
import os, sys, time

def build_ui():
    result = subprocess.run(["pyside6-uic", UI_FILE], capture_output=True, text=True, check=True)
    with open(GEN_FILE, "w", encoding="utf-8") as output_file:
        output_file.write(result.stdout)
    print(f"{UI_FILE} -> {GEN_FILE}")
    print("----------------------------")

def build_exe():
    it = time.time()
    os.system("python -m nuitka --onefile main.py --enable-plugin=pyside6 --windows-console-mode=disable --output-dir=dist")
    elapsed = time.time() - it
    print("----------------------------")
    print(f"Build time: {elapsed:.2f} seconds")
    print("file size of dist/main.exe: " + str(os.path.getsize("dist/main.exe")/1024/1024) + " MB")
try:
    if sys.argv[1] == "ui":
        build_ui()
    elif sys.argv[1] == "exe":
        build_exe()
    elif sys.argv[1] == "all":
        build_ui()
        build_exe()
    else:
        build_ui()
        build_exe()
except IndexError:
    print("Usage: python build.py [ui|exe|all]")