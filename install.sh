#!/usr/bin/env bash

####--------------------------------####
#--# Author:   by Umbrellla777      #--#
#--# Telegram: @Umbrellla_l         #--#
#--# VK:       @Umbrellla777        #--#
####--------------------------------####

# const
readonly version="1.0"
readonly c_error='\033[5m'
readonly c_yellow='\033[33m'
readonly c_red='\033[31m'
readonly c_green='\033[32m'
readonly c_def='\033[0m'

# Update
pkg update -y

# install python
echo "${c_green}[Installation] ${c_def} Python 3"
pkg3 install -y python3
clear

# install Libs for python
echo "${c_green}[Installation] ${c_def} Library telethon for Python"
pip3 install telethon
clear

# Sucsess
cd Umbrellla777-bot-ENG-
mkdir users
chmod +777 start
cp start ~/start
cd ~/
chmod +777 start
echo "${c_green}[Completed]${c_def} The installation is successfully completed!"
echo "${c_green}[Launch]${c_def} Do the following ./start api_id api_hash"
