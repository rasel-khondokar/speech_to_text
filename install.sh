#!/bin/bash
sudo apt-get install libjack-jackd2-dev portaudio19-dev python3-pyaudio portaudio19-dev
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
deactivate