import pyautogui
import requests
import os
from datetime import datetime

# Function to take a screenshot
def take_screenshot():
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    screenshot_filename = f'screenshot_{timestamp}.png'
    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_filename)
    return screenshot_filename

# Function to send the screenshot to a Discord channel
def send_to_discord(screenshot_filename, webhook_url):
    with open(screenshot_filename, 'rb') as f:
        payload = {'file': (screenshot_filename, f, 'image/png')}
        response = requests.post(webhook_url, files=payload)
        if response.status_code == 204:
            print(f'Screenshot {screenshot_filename} sent to Discord channel successfully.')
        else:
            print(f'Failed to send screenshot {screenshot_filename} to Discord channel. Status code: {response.status_code}')

# Replace 'your_webhook_url' with the actual Discord webhook URL
webhook_url = 'your_webhool_url'

# Take a screenshot
screenshot_filename = take_screenshot()

# Send the screenshot to the Discord channel
send_to_discord(screenshot_filename, webhook_url)

# Clean up the screenshot file after sending
os.remove(screenshot_filename)