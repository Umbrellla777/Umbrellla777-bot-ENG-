![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) <br/>
***
Author:   by Umbrellla777 <br/>
Telegram: [@Umbrellla777](https://t.me/Umbrellla777) <br/>
VK:       [@Umbrellla777](https://vk.com/umbrellla777) <br/>
***
> [!IMPORTANT]
> The translation is not accurate (contact me for help with the translation)

> [!NOTE]
> The project is developing and work is underway to add new commands, stay tuned.
# Umbrellla777-bot-ENG-
Python a script for text design in Telegram

# Installation Termux
Termux - this is a free and open source terminal emulator for Android <br/>
There are several options for installing the application: <br/>
* Installation from the [official repository](https://github.com/termux/termux-app?tab=readme-ov-file#termux-app-and-plugins)
  > The Releases panel will show the versions. <br/>
  > Select the version and install it. <br/>
  > Done. <br/>
* Installation via [F-Droid](https://f-droid.org)
  > Installing the application from [website](https://f-droid.org). <br/>
  > You open it and search for Thermex in the search. <br/>
  > Install and run it. <br/>
  > Done. <br/>
* Installation with [4PDA](https://4pda.to/forum/index.php?showtopic=741456)
  > Select the version and install it. <br/>
  > Done. <br/>
  
# After installation Termux
1) Moving on to https://my.telegram.org/apps  <br/>
Enter your phone number in the field **Your Phone Number**  <br/>
After the confirmation code arrives, enter it in the field **Confirmation code**  <br/>
And press the button **Sign In**  <br/>

2) Creating our own "application"
In the field **App Tittle** writing **Your name**  <br/>
In the field **Short** Name writing **Your name**  <br/>
In **Platform** choose **Other**  <br/>
And press button **Create Application**  <br/>

3) We copy it somewhere **api_id** и **api_hash**  <br/>
**api_id** these are numbers like **1234567**  <br/>
**api_hash** these are both letters and numbers of the type **123sdf123sdf234...**  <br/>

4) Open Termux and insert the following command into it:
```bash
pkg update -y
```
```bash
pkg install -y git
```
```bash
pkg install -y python3
```
```bash
git clone https://github.com/Umbrellla777/Umbrellla777-bot-ENG-
```
```bash
cd Umbrellla777-bot-ENG-
```
```bash
sh install.sh
```
I will briefly explain the commands:
```bash
pkg update -y # Checking for package updates and installing them
pkg install -y git # Installing the git version control system
pkg install -y python3 # Installing the YAP Interpreter python 3
git clone https://github.com/Umbrellla777/Umbrellla777-bot-ENG- # After installing git, download the repository with the script
cd Umbrellla777-bot-ENG- # Go to the directory with the script
sh install.sh # Running the script
cd .. # Exit to from the directory Umbrellla777-bot-ENG-
```

After inserting the command, press Enter (new line). <br/>
The script will be installed.  <br/>
If you have done everything correctly, you will see the inscriptions:  <br/>
***[Completed] The installation is successfully completed!"***  <br/>
***[Launch] Do the following./start api_id api_hash"***

5)Running the script.  <br/>
In Termux writing **./start your_api_id your_api_hash**  <br/>
Example of a command **./start 1234567 1d12d45fg56g563**  <br/>
And press Enter. After a couple of seconds, you will be asked to enter your number again, enter, get the code, enter the code and that's it!  <br/>

Upon successful launch, there will be a strip:  <br/>
***[PROFILE: My name | Id: 123345567 | Uname: @MyUserName]***

6) Commands  <br/>
The entire list of commands after starting the bot is called by the command .help <br/>
