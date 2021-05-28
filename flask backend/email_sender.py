import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def send_email(content,dest):
    mail_user = 'robotbytejump@163.com'
    mail_pass = 'VLPQTTLAMHVXPJRL'

    sender = 'robotbytejump@163.com'
    receivers = [dest] 
    content = "请点击下方链接完成验证：\n"+content

    message = MIMEText(content,'plain','utf-8')     
    message['Subject'] = '在线编程面试平台注册验证邮件' 
    message['From'] = formataddr(["验证机器人", sender])
    message['To'] = receivers[0]  

    try:
        smtpObj = smtplib.SMTP_SSL('smtp.163.com')
        smtpObj.login(mail_user,mail_pass) 
        smtpObj.sendmail(sender,receivers,message.as_string())
        smtpObj.quit()
        return True
    except smtplib.SMTPException as e:
        return False
