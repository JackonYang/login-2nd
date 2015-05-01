#!/bin/bash

# PIL
sudo apt-get update
sudo apt-get install libjpeg8-dev zlib1g-dev libfreetype6-dev

sudo ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
sudo ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib
sudo ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib

sudo pip install PIL --allow-external PIL --allow-unverified PIL

sudo ln -s /usr/include/freetype2 /usr/include/freetype

# OCR engine from google
sudo apt-get install  tesseract-ocr

sudo pip install -r requirements.txt
