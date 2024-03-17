# Project Name: Discord Bot
## Author: Daniel Palmer
### Date: 3/17/24
### Description: A python script that takes a screenshot of your screen and uses a webhook to send the screenshot to a discord server. The instructions below can help set the script to run automatically.


Prerequisites: <br>
     - Python installation (version 3.12 recommended). This can be checked by running the command prompt and typing 'python --version' <br>

1. Create a Discord Webhook: <br>
    a. Go to your discord server and generate a webhook. <br>
        -  Discord server > Caret dropdown > Server settings > Integrations > Webhooks > New webhook > Configure the webhook as desired > Copy the webhook URL. <br>

2. Add the Webhook URL to the screenshot.py file: <br>
    a. Open screenshot.py in a text editor. <br>
    b. Insert the webhook URL into the webhook_url variable where directed. <br>

3. Create .bat files to execute the program: <br>
    a. Create a main folder to contain all of the necessary files for the task scheduler. <br>
    b. Create a file named exe.bat: <br>
      ```
      ECHO OFF <br>
      python <screenshot.py full file path> <br>
      ```
      c. Create a file invisible.vbs: <br>
      ```
      CreateObject("Wscript.Shell").Run """" & WScript.Arguments(0) & """", 0, False <br>
      ```
      d. Create the final file, screenshot.bat, to run both files in hidden mode:
      ```
      wscript.exe <invisible.vbs full file path> <exe.bat full file path> <br>
      ```

5. Schedule the screenshot.bat file to run: <br>
    a. Open the Windows Task Scheduler (search for “Task Scheduler” in the Windows search bar). <br>
    b. Click on “Create Basic Task…” on the right side. <br>
    c. Give your task a name and description. <br>
    d. Choose how often you want the script to run (e.g., daily). We can customize this further later. <br>
    e. In the “Actions” tab, select “Start a program” and provide the path to your screenshot.bat file. Under "Start in" provide the path to the folder containing the screenshot.bat file. <br>
    f. Save the task. <br>
    g. Test the Scheduled Task: Wait for the scheduled time, and the script will automatically take a screenshot and send it to your Discord channel. <br>
