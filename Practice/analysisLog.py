#!/usr/bin/python
# encoding=utf-8
# Filename: analysisLog.py
import os, sys, re, time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import datetime
from jinja2 import Environment, FileSystemLoader
import codecs
import MySQLdb

reload(sys)
sys.setdefaultencoding('utf8')

# 执行文件目录
home_dir = "/mnt/ejlomp/syshealthmon"
# 报告模板目录
templates_dir = os.path.join(home_dir,"templates")
# home_dir = "E:\\PythonProject\\ECHARTS"
# 生成报告目录
report_dir = os.path.join(home_dir, "logAnalysis")
# 查看报告地址
report_url = "http://www.runscm.com"
# 查看报告用户名
report_user = "ejlpt_admin"
# 查看报告密码
report_pwd = "yl@1806"
# report_dir = "d:\\"
# 日志文件所在目录
log_home_dir = "/mnt/prodlog"
# 生成异常日志文件目录
result_log_dir = os.path.join(home_dir, "result")
# result_log_dir = "d:\\log\\result"
# 报告文件名
report_file_name = "index.html"
# 日志所在服务器ip
log_env = ['118.178.95.22'+os.linesep]
# 是否分析昨天的日志，若为False则分析当天的日志
is_yesterday = True
# 忽略包含这些关键字的异常信息
ignore_keys = ["isException=0"]
# 忽略包含这些关键字的日志文件
ignore_file = ['sql', 'aspect']
# 日志对应相关负责人
matchup = {"judy":['dts-server-refund', 'excel'], "jessie":['dts-config', 'dts-item-server', 'dts-queue-server', 'dts-server', 'dts-upstream', 'oms', 'oms-sql', 'egenie_oms_batch', 'egenie_dts_server'], "dani":['wms', 'tms', 'tms-rest', 'tms-sql'], "victor,ivy":['egenie', 'egenie_web', 'message', 'baseinfo', 'cache', 'pms'], "rui":[]}
# 发送邮件相关信息
mail_host = "smtp.exmail.qq.com"
mail_user = "ethan@egenie.cn"
mail_pass = "LIming5118"
sender = "ethan@egenie.cn"
# cc = ['ethan@egenie.cn']
cc = ['ethan@egenie.cn', 'terryg@egenie.cn', 'hogan@egenie.cn']

# # 本地数据库信息
# sid = "localhost"
# db_host = "127.0.0.1"
# db_port = 3306
# db_user = "root"
# db_pass = "gloryroad"
# db_db = "test"
# db_charset = "utf8"
# table_name = "analysis_result_module"

# ejl_omp数据库信息
sid = "omp"
db_host = "rm-bp1ov5155kw37fa31i.mysql.rds.aliyuncs.com"
db_port = 3306
db_user = "ejl_omp"
db_pass = "ejlomp@1806"
db_db = "ejl_omp"
db_charset = "utf8"
table_name = "analysis_result_module"

class NewReport(object):
    u"""生成报告类"""
    def __init__(self):
        envPath = os.path.join(home_dir, "templates")
        self.env = Environment(loader = FileSystemLoader(envPath))
        # print envPath

    def render_html(self, **kwargs):
        template = self.env.get_template("analysis_report_temp.html")
        return template.render(**kwargs)

    def create_report(self, reportName, **kwargs):
        filePath = os.path.join(report_dir, reportName)
        renderHtml = self.render_html(**kwargs)
        with codecs.open(filePath, "w", encoding="utf-8") as fp:
            fp.write(renderHtml)

class MysqlManage(object):
    u"""Mysql数据库操作类"""
    def __init__(self):
        self.section = sid
        self.host = db_host
        self.port = db_port
        self.username = db_user
        self.password = db_pass
        self.db = db_db
        self.charset = db_charset
        self.conn = None
        self.cursor = None

    def connect(self):
        u"""连接数据库"""
        try:
            self.conn = MySQLdb.connect(
                host = self.host,
                port = self.port,
                user = self.username,
                passwd = self.password,
                db = self.db,
                charset = self.charset)
        except Exception, e:
            assert 1 == 2 , u"连接数据库：" + self.db + "失败：" + str(e)

    def get_cursor(self):
        self.cursor = self.conn.cursor()
        return self.cursor

    def execute_sql(self, sql):
        u"""执行sql语句"""
        try:
            self.cursor.execute(sql)
        except MySQLdb.Error, e:
            raise Exception(u"Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def executemany_sql(self, sql, datas):
        u"""执行sql语句"""
        try:
            self.cursor.executemany(sql, datas)
        except MySQLdb.Error, e:
            raise Exception(u"Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def get_content(self):
        u"""获取查询结果"""
        try:
            res = self.cursor.fetchone()
            return res
        except MySQLdb.Error, e:
            raise Exception(u"Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def get_content_all(self):
        u"""获取所有查询结果"""
        try:
            resSet = self.cursor.fetchall()
            return resSet
        except MySQLdb.Error, e:
            raise Exception(u"Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def get_content_by_line(self, lines):
        u"""获取指定条数的数据"""
        try:
            resTuple = self.cursor.fetchmany(lines)
            return resTuple
        except MySQLdb.Error, e:
            raise Exception(u"Mysql Error %d: %s" % (e.args[0], e.args[1]))
        finally:
            self.close()

    def commit(self):
        u"""提交事务"""
        try:
            self.conn.commit()
        except MySQLdb.Error, e:
            raise Exception(u"Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def close(self):
        u"""断开连接"""
        try:
            if None == self.cursor:
                pass
            else:
                self.cursor.close()
                self.conn.close()
        except MySQLdb.Error, e:
            raise Exception(u"断开连接失败：" + str(e))

class mail(object):
    u"""发送邮件类"""
    def send_mail(self, mail_host, mail_user, mail_pass, sender, receivers, text, files):
        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = mail_user
        message['To'] = ';'.join(receivers)
        subject = '异常日志'
        message['Subject'] = Header(subject, 'utf-8')

        # 邮件正文内容
        message.attach(MIMEText(text, 'plain', 'utf-8'))

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

        # 发送邮件
        try:
            for i in range(10):
                try:
                    print u"发送邮件中..."
                    smtpObj = smtplib.SMTP_SSL(mail_host, 465)
                    #smtpObj.connect()
                    smtpObj.login(mail_user, mail_pass)
                    # print receivers
                    smtpObj.sendmail(sender, receivers, message.as_string())
                    smtpObj.quit()
                    smtpObj.close()
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
    u"""分析日志文件"""
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

def get_today():
    u"""获取当天的日期yyyy-mm-dd"""
    return datetime.date.today().strftime("%Y-%m-%d")

def get_now_time():
    u"""获取当前的时间yyyy-mm-dd HH:MM:SS"""
    return time.strftime("%Y-%m-%d %H:%M:%S")

def find_yesterday_logfiles(path):
    u"""查找指定目录下的所有昨天的日志文件"""
    log_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if get_yesterday() in file:
                for i in ignore_file:
                    if i in file:
                        break
                else:
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
            if file.endswith(".log") and expect < datetime.datetime.fromtimestamp(os.path.getmtime(file_path)):
                for i in ignore_file:
                    if i in file:
                        break
                else:
                    log_files.append(file_path)
    return log_files

def empty_dir(path):
    u"""清空目录"""
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)

if __name__ == "__main__":
    dd = get_yesterday() if is_yesterday else get_today()
    # 判断分析结果目录是否存在，若不存在则创建目录，若存在则清空
    if not os.path.exists(result_log_dir):
        # 创建目录
        os.mkdir(result_log_dir)
    else:
        # 清空目录
        empty_dir(result_log_dir)
    result_dict = {}
    for arg in sys.argv[1:]:
        log_dir = os.path.join(log_home_dir, arg)
        log_env.append(arg+", ")
        log_name = arg
        files_name = []
        # 获得并遍历所有前一天的日志文件
        for file_path in find_yesterday_logfiles(log_dir) if is_yesterday else find_today_logfiles(log_dir):
            file_name = os.path.splitext(os.path.split(file_path)[1])[0]
            result_file_name = log_name + "__" + file_name + "_analysisResult.log"
            files_name.append(file_path)
            start_time = time.time()
            print get_now_time()+" : "+"开始分析日志文件："+file_path
            print "分析中......"
            result, count = analysisLog(file_path)
            end_time = time.time()
            print get_now_time()+" : "+"分析结束，用时："+ "%.2f" % (end_time-start_time)+"秒"
            print
            # module_name = file_name.split('.')[0]
            result_file_path = os.path.join(result_log_dir, result_file_name)
            if result_dict.has_key(result_file_path):
                result_dict[result_file_path] += count
            else:
                result_dict[result_file_path] = count
            if count > 0:
                if os.path.exists(result_file_path):
                    with open(result_file_path, 'a') as fp:
                        fp.writelines(result)
                else:
                    with open(result_file_path, 'w') as fp:
                        fp.writelines(result)
    receiver = dict.fromkeys(matchup.keys())
    for key in receiver.keys():
        receiver[key] = []
    text_dict = dict.fromkeys(matchup.keys())
    for key in text_dict.keys():
        text_dict[key] = []
    #print receiver
    #modules_name = []
    #error_count = []
    # print result_dict
    result_datas = []
    # 解析异常日志文件名，分配给对应负责人
    for fileName in result_dict.keys():
        for name, key_words in matchup.items():
            module_name = os.path.split(fileName)[1].split('.')[0]
            func_name = module_name.split("__")[1]
            if re.match(r'(.*)-v39', module_name):
                module_name = re.match(r'(.*)-v39', module_name).group(1)
            elif re.match(r'(.*)-\d{4}-\d{2}-\d{2}', module_name):
                module_name = re.match(r'(.*)-\d{4}-\d{2}-\d{2}', module_name).group(1)
            func_name = module_name.split("__")[1]
            try:
                # print func_name
                if result_dict[fileName] == 0:
                    raise
                if func_name not in reduce(lambda x,y:x+y, matchup.values()):
                    print 'rui', module_name
                    if os.path.getsize(fileName) / 1024 / 1024 > 10:
                        text_dict['rui'].append(fileName + "，异常日志文件超过10M，未在附件中，请到服务器上查看" + os.linesep)
                    else:
                        receiver['rui'].append(fileName)
                    #modules_name.append(func_name)
                    #error_count.append(result_dict[fileName])
                    raise
                elif func_name in key_words:
                    print name, module_name
                    if os.path.getsize(fileName) / 1024 / 1024 > 10:
                        text_dict[name].append(fileName + "，异常日志文件超过10M，未在附件中，请到服务器上查看" + os.linesep)
                    else:
                        receiver[name].append(fileName)
                    #modules_name.append(func_name)
                    #error_count.append(result_dict[fileName])
                    raise
            except:
                result_datas.append((module_name, result_dict[fileName], dd))
                break
    print ''.join(log_env)
    for name in receiver.keys():
        # 收件人
        receivers = [username + '@egenie.cn' for username in name.split(',')] + cc
        # 附件
        files = receiver[name]
        # 正文
        text = '环境：'+os.linesep+''.join(log_env) + os.linesep + ''.join(text_dict[name])+os.linesep+'异常日志见附件'+os.linesep+"日志分析报告地址："+os.linesep+report_url+os.linesep+report_user+'/'+report_pwd+os.linesep
        print receivers
        print files
        print text
        if files:
            mail().send_mail(mail_host, mail_user, mail_pass, sender, receivers, text, files)
            # mail().send_mail(mail_host, mail_user, mail_pass, sender, cc, text, files)
    # print modules_name
    # print error_count
    # n = NewReport()
    # n.create_report("analysis_report.html", modules_name=modules_name, error_count=error_count)
    # print result_datas
    # 将结果数据插入到数据库
    if result_datas:
        mm = MysqlManage()
        mm.connect()
        mm.get_cursor()
        mm.executemany_sql("insert into analysis_result_module(module_name,error_count,date) values(%s,%s,%s)", result_datas)
        mm.commit()
        mm.close()
    # 最新一天的统计结果
    results = {}
    # 模块名
    modules_name = []
    # 近一个月的日期
    dates = []
    # 各模块近一个月的数据及近一个月的总数据
    collect_datas = {}
    mm = MysqlManage()
    mm.connect()
    mm.get_cursor()
    mm.execute_sql("select module_name, error_count from analysis_result_module where error_count != 0 and date = '" + dd + "';")
    contents = mm.get_content_all()
    for module_name,count in contents:
        results[module_name.encode('utf8')] = int(count)
    mm.get_cursor()
    mm.execute_sql("SELECT a.module_name FROM " + table_name + " a GROUP BY a.module_name ORDER BY a.module_name;")
    modules_name = ['total'] + [x[0].encode('utf8') for x in mm.get_content_all()]
    for module_name in modules_name:
        collect_datas[module_name] = []
    mm.get_cursor()
    mm.execute_sql("SELECT a.date FROM " + table_name + " a GROUP BY a.date ORDER BY a.date DESC LIMIT 30;")
    dates = [x[0].strftime("%Y-%m-%d") for x in mm.get_content_all()][::-1]
    # mm.get_cursor()
    # # print str(dates).replace('[','(').replace(']',')')
    # mm.execute_sql("SELECT SUM(a.error_count) FROM " + table_name + " a WHERE a.date IN "+str(dates).replace('[','(').replace(']',')')+" GROUP BY a.date;")
    # collect_datas['total'] = [int(x[0]) for x in mm.get_content_all()]
    # print collect_datas
    # for module_name in modules_name[1:]:
    #     mm.get_cursor()
    #     mm.execute_sql("SELECT SUM(a.error_count) FROM " + table_name + " a WHERE a.module_name='" + module_name + "' and a.date IN "+str(dates).replace('[','(').replace(']',')')+" GROUP BY a.date;")
    #     collect_datas[module_name] = [int(x[0]) for x in mm.get_content_all()]
    for date_time in dates:
        exists_module_count = {}
        mm.get_cursor()
        mm.execute_sql("select a.module_name, a.error_count from " + table_name + " a where a.date='" + date_time + "';")
        contents = mm.get_content_all()
        for exist_module_name,count in contents:
            exists_module_count[exist_module_name.encode('utf8')] = int(count)
        for module_name in modules_name[1:]:
            if module_name in exists_module_count.keys():
                collect_datas[module_name].append(exists_module_count[module_name])
            else:
                collect_datas[module_name].append(0)
        collect_datas['total'].append(sum(exists_module_count.values()))
    mm.close()
    # print results
    # 生成报告
    n = NewReport()
    n.create_report(report_file_name, date_time=dd, results=results, modules_name=modules_name, dates=dates, collect_datas=collect_datas)
