# -*- coding: UTF-8 -*-  
''''自动发送测试
author:Amazing
'''
import sys, os, re, urllib, urllib.parse  
import smtplib  
import traceback  
from email.mime.text import MIMEText  
from email.mime.multipart import MIMEMultipart  
  
def sendmail(subject,msg,toaddrs,fromaddr,smtpaddr,password):  
    ''''' 
    @subject:邮件主题 
    @msg:邮件内容 
    @toaddrs:收信人的邮箱地址 
    @fromaddr:发信人的邮箱地址 
    @smtpaddr:smtp服务地址，可以在邮箱看，比如163邮箱为smtp.163.com 
    @password:发信人的邮箱密码 
    '''  
    mail_msg = MIMEMultipart()  
    if not isinstance(subject,str):  
        subject = str(subject, 'utf-8')  
    mail_msg['Subject'] = subject  
    mail_msg['From'] =fromaddr  
    mail_msg['To'] = ','.join(toaddrs)  
    mail_msg.attach(MIMEText(msg, 'html', 'utf-8'))  
    try:  
        s = smtplib.SMTP()  
        s.connect(smtpaddr)  #连接smtp服务器  
        s.login(fromaddr,password)  #登录邮箱  
        s.sendmail(fromaddr, toaddrs, mail_msg.as_string()) #发送邮件  
        s.quit()  
    except Exception as e:  
       print ("Error: unable to send email")  
       print (traceback.format_exc())  
  
if __name__ == '__main__':  
    fromaddr = "14787811497@163.com"  
    smtpaddr = "smtp.163.com"  
    toaddrs = ["602289152@qq.com","17623832981@163.com"]  
    subject = "测试邮件"  
    password = "*************"
    msg = "测试一下"  
    sendmail(subject,msg,toaddrs,fromaddr,smtpaddr,password)  













