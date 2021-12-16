# discord-live-rpc
## Discord Live RPC! (Windows Only)

![Preview](https://user-images.githubusercontent.com/31751427/146377459-e6340e6e-f7f9-4081-904d-c8dccbf1a5c6.png)

A Python Discord RPC script.
- Shows CPU and RAM usage
- Shows what activity you are doing based on what window is active

(All the activity conditionals are hardcoded, feel free to edit it)

### Requirements
- Python3
- Discord

### Setup
- Open [Discord Developer Portal](https://discord.com/developers/applications)
- Create a new application
- Click Rich Presence on the Left Navbar
- Scroll down and upload a new image
- Name it anything you want, remember this name, this will be used later
- Go to General Information and copy the Application ID

### Installation
- Download the repository and unzip it
- Open Command Prompt and navigate to the directory
- Run this command: 
```
py -m pip install -r requirements.txt
```
- Replace line 42 of the code with the Application ID
- Replace line 43 of the code with the image name
- Done!

To run it, just do:
```
py main.py
```

### Troubleshooting
- Make sure you have `Discord Settings > Activity Status > Display current activity as a status message.` turned on.
