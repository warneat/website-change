## website-change

(tl;dr)
get notified, when website changes.


**This script regularly requests a webpage's content (while also handling a basic authentication) and then compares how often a certain substring occurs. If the number of occurencies differ from status quo, it will give you a notification-message via Telegram.**


## Installation and Configuration

#### In terminal:


If necessary, install the python package-manager 'pip3':

	$sudo apt update
	
	$sudo apt install python3-pip
	
Clone this repository:

	$git clone https://github.com/warneat/website-change

To install required Packages, cd into the new directory and run install requirements
	
	$cd website-change
	
	$pip3 install -r requirements.txt
	

### Create a Telegram Bot:
#### On your smartphone:
Talk to Botfather to create a new bot: https://telegram.me/BotFather
	
Send him:

	/newbot

Choose a name and a username for your bot.
Botfather will give you the API-Token to access and control your bot.

#### In terminal:
To configure telegram-send:

	$telegram-send --configure
	
If prompted, add the location where pip3 installed the python modules and packages to PATH (adjust for your environment; the output of the pip-installation probaply gave you a hint)

	$export PATH=/home/pi/.local/bin:$PATH

You will be asked for the API-Token. Enter it.
Open the url and send the given password to the bot.

### Finally
Set your config variables `URL`, `USER`, `PWRD`, `SUBSTRING`, and `SLEEP_SECONDS` at the beginning of the python script with your desired editor. Make sure to insert the whole URL, as your browser might hide something after a "?"

	
**There you have it!** 

**Run the script with** `$python3 website_change.py` **or** (after making i executable with `chmod +x website_change.py`): `$./website_change.py`**.
I highly recommend, using a cronjob on startup (see below)**

Unfortunately, the message 'running...' does not mean, it is working (yet). To get some insight in what is being requested, run `$./website_change_show.py` for a human-readable version in your command-prompt.


### Further reading:

To start the script automatically and keep it running without an open terminal window consider using cronjob on startup with a little delay: 

	$crontab -e
	
For example on a Raspberry Pi add this line at the bottom:

	@reboot sleep 20 && /home/pi/website-change/website_change.py > /dev/null 2>&1

Otherwise you might want to use screen ([ultra-quick tutorial](https://linuxize.com/post/how-to-use-linux-screen/)) via ssh, to keep process running in the background.


### TODO:
- Improve security, e.g do not store password in python script, as it is basically a text file:
	- add configuration dialog?
	- gain more knowledge about config-files.
	- use cloud solution as a capsule? (virtual machine)
- An alternative module with more features 'python-telegram-bot' is now available. >Implement?
- Add feature to request a status message or interact in some way.

#### Feedback is very much apprechiated
