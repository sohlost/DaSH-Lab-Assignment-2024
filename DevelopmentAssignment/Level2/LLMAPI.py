import json
from datetime import datetime
from openai import OpenAI
import os

client = OpenAI()

data = []
mdl = "gpt-4o-mini"

with open('/home/sohlost/DaSH-Lab-Assignment-2024/DevelopmentAssignment/Level1/input.txt', 'r') as file:
    input_lines = file.readlines()

for line in input_lines:
    timesent = datetime.now().timestamp()
    response = client.chat.completions.create(
        model=mdl,
        messages=[
            {"role": "system", "content": "answer in 2-3 lines"},
            {"role": "user", "content": line}
        ]
    )
    timereceived = datetime.now().timestamp()
    obj = {
        "Prompt": line, 
        "Response": response.choices[0].message.content,
        "TimeSent": timesent,
        "TimeRecvd": timereceived,
        "Source": mdl
    }
    data.append(obj)
    with open('/home/sohlost/DaSH-Lab-Assignment-2024/DevelopmentAssignment/Level1/output.json', 'a') as file:
        json.dump(obj, file, indent=4)
        

    




