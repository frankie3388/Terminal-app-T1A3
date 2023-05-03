#!/bin/bash

if [ -f "./roulette-venv/bin/activate" ]; then
    source roulette-venv/bin/activate
    pip3 install -r requirements.txt
    python3 main.py
else
    python3 -m venv roulette-venv
    source roulette-venv/bin/activate
    pip3 install -r requirements.txt
    python3 main.py
fi