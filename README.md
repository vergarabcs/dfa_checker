# DFA slots checker
- This tool partially automates the process of checking for DFA passport slots
- This tool is a gui bot. You will have to manually check the screen if a slot is available.
- Only tested on Windows 1920 x 1080, 100% Chrome browser zoom, 100% windows display settings.

# Requirements
* python 3
* virtualenv (Optional)
* pyautogui

# Setup
1.) Clone repo and change directory
```
$ git clone https://github.com/vergarabcs/dfa_checker.git
$ cd dfa_checker
```

2.) (Optional) Create and activate virtual environment so you don't install globally.
```
$ virtualenv venv
$ source venv/Scripts/activate
```

3.) Install pyautogui
```
$ pip install pyautogui
```

4.) Run dfa.py. This will start the bot. Sometimes, due to dfa updates or other reasons, the bot gets sidetracked, close terminal to stop. You can also modify dfa.py.
```
$ python dfa.py
```

# Screen Cap
![Alt text](/assets/screen_cap.gif "Dfa Gui Bot")
