import subprocess

UI_FILE = "window.ui" 
GEN_FILE = "window_generated.py"

result = subprocess.run(["pyside6-uic", UI_FILE], capture_output=True, text=True, check=True)

with open(GEN_FILE, "w", encoding="utf-8") as output_file:
    output_file.write(result.stdout)

print(f"{UI_FILE} -> {GEN_FILE}")