# grabble-bot
My friend somehow keeps finding more and more obscure word games so here is a bot for the game "grabble"

You can play grabble at https://grabble.coolmathgames.com/new-home

# Installation
This bot requires python to run so if you dont already have python go get the latest version from: https://www.python.org/downloads/

Once you have installed python open cmd and move the the directory where you downloaded the bot (Usually in your downloads folder)

Then run
```
python Main.py
```

It should open a new Chrome window with grabble open

By default the Chrome window is muted so that when the bot tries all the words it finds it doesnt make a loud noise


# Features
The bot is currently configured to grab new words as fast as possible and it will constantly try and steal opponent's words and improve its own

A demo
![grabble-demo](https://user-images.githubusercontent.com/68296986/132135716-05f2a73e-edf0-44af-b91a-50fb2884729d.gif)

# Troubleshooting
If the Chrome window does not open, then open your normal google chrome and check what version (`9x.x.xxxx.xxx`) you have (you can find this in the about tab in settings) 

Then download that version from https://chromedriver.chromium.org/downloads and replace the one in the current version 

For example if you have version 92.0.4515.159 you would download the ChromeDriver for version 92.

# 

Thanks to https://github.com/tinmarr/Word-Unscrambler for the unscramble.py (It made my life a lot easier)
