#encoding:utf-8
'''
Created on 2012/4/22
Updated on 2014/5/2

@author: bhchen
'''

import sys,random,os
import mailsender

inf = open(sys.argv[1])
outf = open(sys.argv[2],'w')

lines = inf.readlines()

num = []    #學號
mail_address = []   #電子郵件位址

mail_host = ""      #mail_host, ex:smtp.gmail.com
mail_port = ""      #mail_port, ex:587(gmail)
mail_postfix = ""   #postfix, ex:gmail.com
account = ""
passwd = ""
sender = mailsender.sendmail(mail_host,mail_port,mail_postfix,account,passwd)

for line in lines:
    num.append(line.split(",")[0])
    mail_address.append(line.split(",")[1].split()[0])

for i in range(len(num)):
    account = num[i]
    random_char = random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 6)
    passwd = ""
    for j in range(len(random_char)):
        passwd += random_char[j]

    #create帳號
    useradd = "useradd -b /home/ -m -s /bin/bash " + account
    os.system(useradd)
    set_passwd = "echo " + account + ":" + passwd + " | chpasswd"
    os.system(set_passwd)

    #將帳號密碼寄出
    subject = "subject"
    content = "content"
    mailto  =  mail_address[i]
    sender.send(subject, content, mailto)
    
    outf.write(account + "," + passwd + "\n")
    
inf.close()
outf.close()