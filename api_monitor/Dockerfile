#Base Operating System 

FROM python:3.9-slim

#Workbench
WORKDIR /app

#The Setup

RUN pip install requests

#Payload

COPY . . 

#Copy payload from windows folder to Container 

#The Command 
#What happens when container initiates 

CMD ["python", "spy.py"]
