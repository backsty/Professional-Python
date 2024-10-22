import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Mail:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.smpt_address = "smtp.gmail.com"
        self.imap_address = "imap.gmail.com"
        self.header = None

    def send_mail(self, recipients, subject, message_text):
        message_ = MIMEMultipart()
        message_['From'] = self.login
        message_['To'] = ', '.join(recipients)
        message_['Subject'] = subject
        message_.attach(MIMEText(message_text))
        message_sender = smtplib.SMTP(self.smpt_address, 587)
        # identify ourselves to smtp gmail client
        message_sender.ehlo()
        # secure our email with tls encryption
        message_sender.starttls()
        # re-identify ourselves as an encrypted connection
        message_sender.ehlo()
        message_sender.login(self.login, self.password)
        message_sender.sendmail(self.login, recipients, message_.as_string())
        message_sender.quit()

    def receive_email(self) -> str:
        message_receiver = imaplib.IMAP4_SSL(self.imap_address)
        message_receiver.login(self.login, self.password)
        message_receiver.list()
        message_receiver.select("inbox")
        criterion = '(HEADER Subject "%s")' % self.header if self.header else 'ALL'
        data = message_receiver.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        data = message_receiver.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        message_receiver.logout()
        return email_message.as_string()


if __name__ == '__main__':
    login = 'login@gmail.com'
    password = 'qwerty'
    subject = 'Subject'
    recipients = ['vasya@email.com', 'petya@email.com']
    message = 'Message'
    mail = Mail(login, password)
    mail.send_mail(recipients, subject, message)
    print(mail.receive_email())
