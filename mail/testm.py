# coding: utf-8
import smtplib
import time
from email.mime.text import MIMEText
from email.header import Header

nowtime = time.strftime('%Y-%m-%d-%H:%M', time.localtime(time.time()))
sender = 'guocai666@21cn.com'
receiver = ['mortimer2017@163.com']
subject = 'ServerError at {}'.format(nowtime)
smtpserver = 'smtp.21cn.com'
username = sender
password = 'l7hqfr'

for i in receiver:
    msg = MIMEText('ServerError at {} please fix it'.format(nowtime), 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = i
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, i, msg.as_string())
    smtp.quit()