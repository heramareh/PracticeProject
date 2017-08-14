#!/usr/bin/python
# encoding=utf-8
# Filename: analysisLog.py
import os, sys, re, time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import datetime

ignore_keys = ["isException=0"]

def send_mail(mail_host, mail_user, mail_pass, sender, receivers, files):
    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = mail_user
    message['To'] = ';'.join(receivers)
    subject = '异常日志'
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
                print u"发送邮件中..."
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

def analysisLog(file_name):
    global ignore_keys
    n = 100
    result = ["*"*n+os.linesep]
    one_log = ''
    r = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
    count = 0
    with open(file_name) as fp:
        for each_line in fp:
            if re.match(r, each_line):
                if "Exception" in one_log:
                    for ignore_key in ignore_keys:
                        if ignore_key in one_log:
                            break
                    else:
                        result.append(one_log+os.linesep)
                        result.append("*"*n+os.linesep)
                        count += 1
                one_log = ''
            one_log += each_line
        else:
            if "Exception" in one_log:
                for ignore_key in ignore_keys:
                    if ignore_key in one_log:
                        break
                else:
                    result.append(one_log + os.linesep)
                    result.append("*" * n + os.linesep)
                    count += 1
                
    return result, count

def get_yesterday():
    u"""获取前一天的日期yyyy-mm-dd"""
    yesterday = datetime.date.today() + datetime.timedelta(days=-1)
    return yesterday.strftime("%Y-%m-%d")

def find_yesterday_logfiles(path):
    u"""查找指定目录下的所有昨天的日志文件"""
    log_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if get_yesterday() in file:
                log_files.append(os.path.join(root, file))
    return log_files

def find_today_logfiles(path):
    u"""查找指定目录下当天的所有日志文件"""
    log_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            now = datetime.datetime.now()
            expect = now.replace(hour=0, minute=0, second=0,microsecond=0)
            if file.endswith(".log") and expect < datetime.datetime.fromtimestamp(os.path.getctime(file_path)):
                log_files.append(file_path)
    return log_files

def empty_dir(path):
    u"""清空目录"""
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)

if __name__ == "__main__":
    result_log_dir = "/mnt/log/result"
    empty_dir(result_log_dir)
    result_dict = {}
    for arg in sys.argv[1:]:
        files_name = []
        for file_path in find_yesterday_logfiles(arg):
            file_name = os.path.splitext(os.path.split(file_path)[1])[0]
            result_file_name = file_name + "_analysisResult.log"
            files_name.append(file_path)
            result, count = analysisLog(file_path)
            module_name = file_name.split('.')[0]
            if result_dict.has_key(module_name):
                result_dict[module_name] += count
            else:
                result_dict[module_name] = count
            result_file_path = os.path.join(result_log_dir, result_file_name)
            if count > 0:
                if os.path.exists(result_file_path):
                    with open(result_file_path, 'a') as fp:
                        fp.writelines(result)
                else:
                    with open(result_file_path, 'w') as fp:
                        fp.writelines(result)
    for k,v in result_dict.items():
        print k,v
    # mail_host = "smtp.exmail.qq.com"
    # mail_user = "ethan@egenie.cn"
    # mail_pass = "LIming5118"
    # sender = "ethan@egenie.cn"
    # receivers = ['ethan@egenie.cn']
    # send_mail(mail_host, mail_user, mail_pass, sender, receivers, files_name)
    # for i in find_today_logfiles("d:\\log"):
    #     print i