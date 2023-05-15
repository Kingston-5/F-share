#!/bin/bash

# -------------------------------
# Info:
#   author	: Kingston-5
#   file	: setup.sh
#   created	: 16/05/23
#   version	: 0.1
# -------------------------------
# Requirements:
#   python
# Description:
#   Setup Shell Script of youtube-dl Downloader for Termux in Android.
#
# -------------------------------

## checking python installation
echo  "Installing F-share"
echo  "checking python installation"
if command -v python >/dev/null 2>&1; then

  # Python 3 is installed, print a string
  echo "Python 3 is installed!"

else

  # Python 3 is not installed, exit
  echo "Python 3 is not installed."
  echo "Please install min v3 of python."
  exit 1

fi
sleep 2

echo "setting up termux storage"
termux-setup-storage
sleep 2

echo  "Storage Setup Completed"
sleep 2

## Update Termux repository and packages.
echo  "Updatting Termux repository and packages"
echo  ""

apt update && apt upgrade -y

echo  ""
echo  "Update completed"
sleep 2

echo  "Preparing Installation"
echo  ""
sleep 2

cd ~/
