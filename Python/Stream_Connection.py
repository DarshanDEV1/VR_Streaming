import pyautogui
import keyboard
import os
import time
import subprocess

#Boolean that is used to stop or start
_STARTorSTOP = False

# Path to save screenshots
path_to_save_screenshots = "C:/Users/Drz_404_DT/Desktop/screenshots"

# Function to take a screenshot
def take_screenshot(_value):
	_STARTorSTOP = _value
	while(_STARTorSTOP == True):
    		screenshot = pyautogui.screenshot()
    		screenshot_path = os.path.join(path_to_save_screenshots, f"screenshot_{time.time()}.png")
    		screenshot.save(screenshot_path)
    		send_to_android(screenshot_path)
    		time.sleep(.0001)

# Function to send the screenshot to the Android device
def send_to_android(screenshot_path):
    adb_mkdir_command = ["adb", "shell", "mkdir", "-p", "/sdcard/screenshots/"]
    subprocess.run(adb_mkdir_command, check=True)
    adb_push_command = ["adb", "push", screenshot_path, "/sdcard/screenshots/"]
    subprocess.run(adb_push_command, check=True)
    time.sleep(.001)
    os.remove(screenshot_path)  # Delete the screenshot after sending it
    adb_rm_command = ["adb", "shell", "rm", "/sdcard/screenshots/" + os.path.basename(screenshot_path)]
    subprocess.run(adb_rm_command, check=True)  # Delete the screenshot from the Android device

# Listen for 'P' key to take a screenshot
keyboard.add_hotkey('p', take_screenshot(True))

# Listen for 'Q' key to stop the application
#keyboard.wait('q')
keyboard.add_hotkey('q', take_screenshot(False))
