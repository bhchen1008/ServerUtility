#encoding:utf-8
'''
This is a mail sender.
You can call this python code to send mail.
EX:
This name of file is mail_sender.

import mail_sender

$mail_host,$mail_user,$mail_passwd,$subject,$content,$mailto are provided by user.
$mail_host: mail host like "smtp.mail.com"
$mail_user: account of mail
$mail_passwd: password of mail
$mailto: mail to who?
sender = mail_sender.sendmail($mail_host,$mail_user,$mail_passwd)
sender.send($subject,$content,$mailto)
'''
import smtplib
from email.mime.text import MIMEText

class sendmail:
    def __init__(self,mail_host,mail_port,postfix,mail_user,mail_passwd):
#        self.mail_host="smtp.mail.com"
        self.mail_host = mail_host #like smtp.gmail.com
	self.mail_port = mail_port
        self.mail_user = mail_user
        self.mail_passwd = mail_passwd
        self.postfix = postfix
    def send(self,subject,content,mailto):
        mailuser=self.mail_user+"@"+self.postfix
        msg = MIMEText(content)                  
        msg['Subject'] = subject                    
        msg['From'] = "me"
        msg['To'] = mailto
        smtp = smtplib.SMTP(self.mail_host,self.mail_port)         
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(self.mail_user,self.mail_passwd)
        smtp.sendmail(mailuser,mailto,msg.as_string()) #parameter mailuser很重要，若空白的話會被冠上可能是非account@gmail.com所發出，以至於有些信箱會將此種信擋掉
        smtp.close()
        print "Mail is sent successfully!"
