import pyautogui
import numpy as np
import cv2
import subprocess
import os
import keyboard
import time

def capture_and_send_screenshot():
    # Capture screenshot
    screenshot = pyautogui.screenshot()

    # Convert the image into numpy array representation
    img = np.array(screenshot)

    # Convert the image into bytes
    img_data = cv2.imencode('.png', img)[1].tobytes()

    # Save the image data to a file
    with open('screenshot.png', 'wb') as f:
        f.write(img_data)

    # Send the file to the Android device
    adb_push_command = ["adb", "push", "screenshot.png", "/sdcard/"]
    subprocess.run(adb_push_command, check=True)

    # Delete the screenshot after sending it
    os.remove('screenshot.png')

# Run the function in a loop until 'q' is pressed
while True:
    capture_and_send_screenshot()
    time.sleep(.001)
    if keyboard.is_pressed('q'):
        break
