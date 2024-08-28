#!/bin/bash

python3 serverside.py &
sleep 2

for i in {1..12}
do
     python3 clientside.py $i input.txt &
done

wait