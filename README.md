# GroupMeDiscord

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f75c31c547204176a8e8dc4412918b17)](https://app.codacy.com/app/AnonGuy/GroupMeDiscord?utm_source=github.com&utm_medium=referral&utm_content=AnonGuy/GroupMeDiscord&utm_campaign=Badge_Grade_Dashboard) [![Build Status](https://travis-ci.org/AnonGuy/GroupMeDiscord.svg?branch=master)](https://travis-ci.org/AnonGuy/GroupMeDiscord) [![Updates](https://pyup.io/repos/github/AnonGuy/GroupMeDiscord/shield.svg)](https://pyup.io/repos/github/AnonGuy/GroupMeDiscord/)


Some Python scripts to interface between Discord and GroupMe.

## Requirements
These scripts require Python 3.6+. <br/>
Before starting, make sure that you install the requirements with:
```bash
cd ~/path/to/GroupMe/
python3 -m pip install -r requirements.txt
```
If you have issues with the discord.py installation, use the following command:
```bash
python3 -m pip install -U https://github.com/Rapptz/discord.py/archive/rewrite.zip#egg=discord.py
```
You also need to be able to **expose the flask webserver.** <br/>
If you already know how to do this, change the `run_locally` variable in `config.ini` to `false`. <br/> <br/>
If not, The easiest method to do this is by using the ngrok tool. View the documentation [here](https://ngrok.com/). <br/>
Once ngrok is setup and authorized, execute the following command to recieve your ngrok URL (you'll need this later):
```bash
ngrok http 5000
```
Keep this process running as you start the application.
### Discord Bot
In order to send messages from Discord to GroupMe, you will need to create a Bot Application. <br>
To do this, first go to https://discordapp.com/developers/applications/me and login with your Discord account. 
Click "New App", fill in your App name, then click "Create App".
![image](http://i.imgur.com/s7QbeCv.png) <br/>
You should be redirected to the application page of your bot. <br/> Scroll down to the following prompt and select "Create a Bot User": <br/>
![image](http://i.imgur.com/C8W4dw1.png) <br/>
You will now be able to view the token of your bot application.
![image](http://i.imgur.com/ODQDOFc.png) <br/>
Copy this token and paste it into your `config.ini` file:
![image](http://i.imgur.com/tdSyCmu.png) <br/>

### Webhook
The webserver will be sending GroupMe messages to a dedicated channel by using a Discord Webhook. <br/>
To create a webhook, navigate to a channel's edit page and select "Webhooks". <br>
After creating a webhook, copy the webhook URL shown: <br/>
![image](http://i.imgur.com/rYzZ9gc.png) <br/>
And paste it into your config file:
![image](http://i.imgur.com/ZMHYt3y.png) <br>
There's just one more thing to do on the Discord side: enable User Settings -> Appearance -> Developer Mode and right click the channel that the webhook is using. Paste this number into your config file too:
![image](http://i.imgur.com/ZbQH1bm.png) <br/>

## GroupMe
Now that you've set up the Discord constants, you'll also need to setup your GroupMe Bot. <br/>
Navigate to https://dev.groupme.com/bots, login with your GroupMe account, and click "Create Bot".
![image](http://i.imgur.com/uEAkype.png) <br/>
Fill in the appropriate fields, and in the **Callback URL** field, enter the URL that you got from ngrok.
![image](http://i.imgur.com/rrUasK3.png) <br/>
Once you've created the Bot, click on the bot's field to see the **Bot ID**. Copy this string and paste it in your config file: <br/>
![image](http://i.imgur.com/hRqS0JM.png)
![image](http://i.imgur.com/nooiph0.png) <br/>
One more to go! On the same page, click the "Access Token" button to retrieve your access token.
Copy this string and paste it into your config file: <br/>
![image](http://i.imgur.com/IpouBmi.png)
![image](http://i.imgur.com/sA8tZJU.png) <br/>

## Usage
Now run the application:
```bash
python3 main.py
```
You should see any messages appear in the chosen Discord channel, and you will also be able to send messages and images to the GroupMe chat.
