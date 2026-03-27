import json
import brain
from twilio.rest import Client
from dotenv import load_dotenv
import os


load_dotenv()
account_sid = os.getenv("account_sid") 
auth_token =  os.getenv("auth_token")

client = Client(account_sid, auth_token)


with open("timetable.json", encoding="utf-16") as time_table:
    data = json.load(time_table)


weekday = brain.weekday
toatal_classes =len(data[weekday])


current_time = brain.current_time

for i in range(toatal_classes):
    start_time = data[weekday][i]['start']
    

    
    
    if start_time[:2] == current_time[:2]:
        
        class_start_time = int(start_time[3:]) - int(current_time[3:])
        if class_start_time < 10 and class_start_time > 0:
            
           subject = data[weekday][i]['subject']
           room =  data[weekday][i]['room']
           faculty = data[weekday][i]['faculty']
        
        mess_ = f"Hello Vivek, today is {weekday}. Your class for {subject}, conducted by {faculty} in room {room}, will begin in {class_start_time} minutes."
        message = client.messages.create(
                    body = f"{mess_}",
                    from_="+13606547194",
                    to="+917456996335")
        
        
   
            