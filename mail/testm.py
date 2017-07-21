# coding: utf-8
import smtplib
import time
from email.mime.text import MIMEText
# from email.header import Header

nowtime = time.strftime('%Y-%m-%d-%H:%M', time.localtime(time.time()))
sender = 'mortimer2017@163.com'
receiver = ['328624847@qq.com']
subject = 'ServerError at {}'.format(nowtime)
smtpserver = 'smtp.163.com'
username = sender
password = 'wyc12345'

for i in receiver:
    msg = MIMEText('ServerError at {} please fix it'.format(nowtime), 'plain',
                   'utf-8')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = i
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, i, msg.as_string())
    smtp.quit()
