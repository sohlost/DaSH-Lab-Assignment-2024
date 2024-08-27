#!/bin/bash


python3 serverside.py &
sleep 2

python3 clientside.py input1.txt output1.json &


wait