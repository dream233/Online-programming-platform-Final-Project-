from re import sub
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def send_email(subject,content,dest):
    """发送邮件
    subject:邮件主题
    content:邮件正文
    dest:目标邮箱
    """
    mail_user = 'robotbytejump@163.com'
    mail_pass = 'VLPQTTLAMHVXPJRL'

    sender = 'robotbytejump@163.com'
    receivers = [dest]

    message = MIMEText(content,'plain','utf-8')     
    message['Subject'] = subject
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

def send_reg_email(content,dest):
    """发送注册验证邮件
    content:注册url
    dest:目标邮箱
    """
    content = "请点击下方链接完成验证：\n"+content
    subject = '在线编程面试平台注册验证邮件'
    return send_email(subject,content,dest)
    
def send_forgetpwd_email(content,dest):
    """发送密码
    content:发送的密码
    dest:目标邮箱
    """
    content = "您的密码是：\n"+content
    subject= "在线编程面试平台忘记密码处理邮件"
    return send_email(subject,content,dest)
