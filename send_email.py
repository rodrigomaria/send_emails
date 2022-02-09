import codecs
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from constants import EMAIL_FROM, EMAIL_TO, PASSWORD

email_from = EMAIL_FROM
email_to = EMAIL_TO

msg = MIMEMultipart("alternative")
msg["Subject"] = "E-mail example using HTML and CSS"
msg["From"] = email_from
msg["To"] = email_to

html_file = codecs.open("email.html", "r", "utf-8")

content = MIMEText(html_file.read(), "html")

msg.attach(content)

mail = smtplib.SMTP("smtp.gmail.com", 587)
mail.ehlo()
mail.starttls()
mail.login(email_from, PASSWORD)
mail.sendmail(email_from, email_to, msg.as_string())
mail.quit()
