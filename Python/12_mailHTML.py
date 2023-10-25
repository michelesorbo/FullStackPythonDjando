import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 587
smtp_server = 'sandbox.smtp.mailtrap.io'
login = '02241113486101'
password = '676068fa22d554'

sender_mail = "miamail@exemple.com"
reciver_mail = 'reciver@exemple.com'
message = MIMEMultipart("alternative")
message['Subject'] = "multipart test"
message['From'] = sender_mail
message['To'] = reciver_mail

#Quando si inviano mail in formato HTML si deve sempre creare l'alternativa con solo testo

text = """\
Ciao,
Sono la mail in formato testuale
"""

#La scrivo in formato HTML
html = """\
<html>
<body>
<p>Ciao, <br>
Sono la mail in formato HTML
<a href="https://google.com">Vai su Google</a>
</p>
</body>
</html>
"""

#Convertiamo le parti in MIMEText
part1 = MIMEText(text,"plain")
part2 = MIMEText(html, "html")
message.attach(part1)
message.attach(part2)

#Invio la mail
with smtplib.SMTP(smtp_server, port) as server:
    server.login(login,password)
    server.sendmail(
        sender_mail, reciver_mail, message.as_string()
    )

print("Mail inviata")
