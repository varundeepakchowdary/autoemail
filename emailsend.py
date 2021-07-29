import smtplib
from email.message import EmailMessage

email = EmailMessage()
email["from"]= "Internship"
email["to"]=["gmail of the person u want to send"]
email["subject"]="Congrats On Getting Selected"
email.set_content("Hey, You got selected for this intern")
with smtplib.SMTP(host="smtp.gmail.com" , port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("gmail","password")
    smtp.send_message(email)
    print("prank done")

