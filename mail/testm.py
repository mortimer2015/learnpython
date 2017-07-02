# coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'mortimer2017@163.com'
receiver = ['328624847@qq.com']
subject = '服务器故障'
smtpserver = 'smtp.163.com'
username = sender
password = 'wyc12345'

for i in receiver:
    msg = MIMEText('请查看监控，判断问题并处理', 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = i
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, i, msg.as_string())
    smtp.quit()