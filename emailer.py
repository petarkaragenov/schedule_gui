import smtplib
import sqlite3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, time, timedelta
from controllers.appointments_controller import AppointmentsController
import dotenv
import os

dotenv.load_dotenv()

SERVER = 'smtp.gmail.com'
PORT = 587
FROM = os.environ.get("FROM")
TO = os.environ.get("TO")
PASS = os.environ.get("PASSWORD")

con = sqlite3.connect("appointments.db")
cur = con.cursor()
content = ""
subject = "Schedule "

now = datetime.now()
today = now.strftime("%A")
tomorrow = now+timedelta(days=1)

if today == "Sunday":
    start = tomorrow.strftime("%Y-%m-%d")
    end = (now+timedelta(days=7)).strftime("%Y-%m-%d")
    content += "<h3>Weekly Schedule</h3><br>"
    subject += "KW" + tomorrow.strftime("%W")

    appointments = AppointmentsController(con, cur).find_many_per_time_period(start, end)["appointments"]
else:
    date = tomorrow.strftime("%Y-%m-%d")
    content += "<h2>Daily Schedule</h2><br>"
    date_format = date.split("-")
    date_format.reverse()
    date_format = '.'.join(date_format)
    subject += date_format

    appointments = AppointmentsController(con, cur).find_many_by_date(date)["appointments"]

if len(appointments) == 0:
    content += "You have no appointments."
else:
    for appointment in appointments:
        _, d, time, place, event, other = appointment
        content += f"<p><b>{event}</b> on <b>{d}</b> at <b>{time}</b> in <b>{place}</b>. (<i>{other}</i>)</p>"

msg = MIMEMultipart()

msg['Subject'] = subject
msg["From"] = FROM
msg["To"] = TO

msg.attach(MIMEText(content, 'html'))

print("Initializing Server...")

server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print("Email Sent...")

server.quit()
