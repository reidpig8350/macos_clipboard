import subprocess

def get_clipboard():
    return subprocess.run(["pbpaste"], capture_output=True, text=True).stdout.strip()

def set_clipboard(text):
    subprocess.run(["pbcopy"], input=text, text=True)