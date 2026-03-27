from flask import Flask
import json
import brain
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def run():
    account_sid = os.getenv("TWILIO_SID")
    auth_token = os.getenv("TWILIO_AUTH")
    client = Client(account_sid, auth_token)

    with open("timetable.json") as time_table:
        data = json.load(time_table)

    weekday = brain.weekday
    current_time = brain.current_time

    total_classes = len(data[weekday])

    for i in range(total_classes):
        start_time = data[weekday][i]['start']

        start = int(start_time[:2]) * 60 + int(start_time[3:])
        current = int(current_time[:2]) * 60 + int(current_time[3:])
        diff = start - current

        if 0 < diff <= 10:
            subject = data[weekday][i]['subject']
            room = data[weekday][i]['room']
            faculty = data[weekday][i]['faculty']

            message = f"Hey Vivek! It's {weekday}. Your {subject} class with {faculty} in room {room} starts in {diff} minutes."

            client.messages.create(
                body=message,
                from_="+13606547194",
                to="+917456996335"
            )

            return "Message Sent"

    return "No class in next 10 minutes"


if __name__ == "__main__":
    app.run()