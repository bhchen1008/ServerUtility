#encoding:utf-8
'''
Created on 2012/4/22

@author: bhchen
'''

import sys,random,smtplib,os

inf = open(sys.argv[1])
outf = open(sys.argv[2],'w')

lines = inf.readlines()

num = []    #學號
mail_address = []   #電子郵件位址

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
    useradd = "useradd -d /home/toc/" + account + " " + account
    os.system(useradd)
    set_passwd = "echo " + passwd + " | passwd --stdin " + account
    os.system(set_passwd) 
    
    #將帳號密碼寄出
    fromaddr = 'your mail'  
    toaddrs  =  mail_address[i]
    #msg = 'There was a terrible error that occured and I wanted you to know!'  
    SUBJECT = "Subject"
    
    TEXT = "Content"   
 
    #(['abcdefghijklmnopqrstuvwxyz',4])
    msg = 'Subject: %s\n%s' % (SUBJECT, TEXT)
    
    # Credentials (if needed)  
    username = 'account'    #gmail帳號  
    password = 'password'    #gmail密碼
    
    # The actual mail send  
    server = smtplib.SMTP('smtp.gmail.com:587')  
    server.starttls()  
    server.login(username,password)  
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
                
    outf.write(account + "," + passwd + "\n")
    
inf.close()
outf.close()

    



