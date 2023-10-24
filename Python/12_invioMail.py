#Invio di email di testo
import unittest #Serve per testare il programma
import smtplib

from email.message import EmailMessage #Serve per precompilare il messaggio della mail

class EmailTestCase(unittest.TestCase):

    def test_mailtrap(self):
        email_ricevente = 'chiriceve@exemple.com'
        email_invio = 'miamiail@exemple.com'
        oggetto = 'Oggetto test mail'
        corpo = 'Sono il corpo della mail. Ciao da Python'

        msg = EmailMessage() #Istanza della classe EmailMassage()

        msg['From'] = email_invio
        msg['To'] = email_ricevente
        msg['Subject'] = oggetto
        msg.set_content(corpo)

        with smtplib.SMTP('sandbox.smtp.mailtrap.io', 2525) as server:
            server.login('02241113486101','676068fa22d554')
            server.send_message(msg)

#Creo il test
if __name__ == '__main__':
    unittest.main()