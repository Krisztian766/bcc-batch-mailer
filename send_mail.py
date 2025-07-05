import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
import json
import csv


load_dotenv()

smtp_server = os.getenv("SMTP_SERVER")
smtp_port = int(os.getenv("SMTP_PORT"))
smtp_user = os.getenv("SMTP_USERNAME")
smtp_pass = os.getenv("SMTP_PASSWORD")
target_link = os.getenv("TARGET_LINK")


with open("template2.html", "r", encoding="utf-8") as file:
    html_body = file.read()

html_body = html_body.replace("{{target_link}}", target_link)


with open("template.json", "r", encoding="utf-8") as f:
    metadata = json.load(f)

subject = metadata["subject"]
from_addr = metadata["from"]


recipients = []
with open("recipients.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        email = row.get("email")
        if email:
            recipients.append(email.strip())


msg = MIMEText(html_body, "html")
msg["Subject"] = subject
msg["From"] = from_addr
msg["To"] = ""
msg["Bcc"] = ", ".join(recipients)


try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.sendmail(from_addr, recipients, msg.as_string())
    print(f" Email sent to {len(recipients)} recipients.")
except Exception as e:
    print(" Error occurred while sending the email:")
    print(str(e))

