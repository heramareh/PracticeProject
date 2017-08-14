#encoding=utf-8

import smtplib
import traceback
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import zipfile, os

def send_mail(files):
    # 第三方 SMTP 服务
    mail_host = "smtp.exmail.qq.com"
    mail_user = "ethan@egenie.cn"
    mail_pass = "LIming5118"
    sender = "ethan@egenie.cn"
    receivers = ['ethan@egenie.cn']

    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = mail_user
    message['To'] = ';'.join(receivers)
    subject = '自动化测试结果'
    message['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    message.attach(MIMEText('异常日志见附件\n', 'plain', 'utf-8'))

    # 构造附件1，传送当前目录下的 test.txt 文件
    for file_name in files:
        #att1 = MIMEText(open(log_file_path, 'rb').read(), 'base64', 'utf-8')
        with open(file_name, 'rb') as fp:
            content = fp.read()
        att1 = MIMEText(content, 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename='+os.path.split(file_name)[1]
        message.attach(att1)

    try:
        for i in range(10):
            try:
                smtpObj = smtplib.SMTP_SSL(mail_host, 465)
                # smtpObj.connect()
                smtpObj.login(mail_user, mail_pass)
                smtpObj.sendmail(sender, receivers, message.as_string())
                smtpObj.quit()
                print u"邮件发送成功"
                break
            except Exception, e:
                print u"邮件发送失败，尝试再次发送......"
                if i == 9:
                    raise e
                else:
                    continue

    except Exception:
        print u"邮件发送失败"



if __name__ == '__main__':
    files=[]
    send_mail(files)
