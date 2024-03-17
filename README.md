Author: Daniel Palmer
Date: 3/17/24
Project Name: Discord Bot

Prerequisites: 
    * Python installation (version 3.12 recommended). This can be checked by running command prompt and typing 'python --version'

1. Create a Discord Webhook: 
    a. Go to your discord server and generate a webhook.
        -  Discord server > Caret dropdown > Server settings > Integrations > Webhooks > New webhook > Configure the webhook as desired > Copy the webhook URL.

2. Add the Webhook URL to the screenshot.py file:
    a. Open screenshot.py in a text editor.
    b. Insert the webhook URL into the webhook_url variable where directed.

3. Create .bat files to execute the program:
    a. Create a main folder to contain all of the necessary files for the task scheduler.
    b. Create a file named exe.bat:
        ECHO OFF
        python <screenshot.py full file path>
    c. Create a file invisible.vbs:
        CreateObject("Wscript.Shell").Run """" & WScript.Arguments(0) & """", 0, False
    d. Create the final file, screenshot.bat, to run both files in hidden mode: wscript.exe <invisible.vbs full file path> <exe.bat full file path>

4. Schedule the screenshot.bat file to run:
    a. Open the Windows Task Scheduler (search for “Task Scheduler” in the Windows search bar).
    b. Click on “Create Basic Task…” on the right side.
    c. Give your task a name and description.
    d. Choose how often you want the script to run (e.g., daily). We can customize this further later.
    e. In the “Actions” tab, select “Start a program” and provide the path to your screenshot.bat file. Under "Start in" provide the path to the folder containing the screenshot.bat file.
    f. Save the task.
    g. Test the Scheduled Task: Wait for the scheduled time, and the script will automatically take a screenshot and send it to your Discord channel.