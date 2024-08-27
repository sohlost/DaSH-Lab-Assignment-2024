#!/bin/bash


python3 serverside.py &
sleep 2

python3 clientside.py input3.txt output3.json &


wait