'''
pip -V                  查看pip版本
pip list                查看所有已安装的包
pip freeze              查看所有已安装的包（处了自带的pip，setuptools等）
pip show package        显示包详情
pip install package     安装包（默认从国外的网站下载安装）
       pip install package -i 国内源
              清华源：https://pypi.tuna.tsinghua.edu.cn/simple
              阿里源：http://mirrors.aliyun.com/pypi/simple/
              豆瓣源：https://pypi.douban.com/simple/
                     pip install -i https://pypi.douban.com/simple/ numpy
                     pip install -i https://pypi.douban.com/simple/--trusted-host pypi.douban.com  #此参数“--trusted-host”表示信任，如果上一个提示不受信任，就使用这个
pip uninstall package    卸载包
'''

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from email.header import Header

class Email():

    def send_email(self, report_name):
        # ZMKACXKVUJRABFHV
        # KKNCDTGXBBOUXEBB

        # smtp服务器
        smtpserver = 'smtp.163.com'

        sender = '18813018625@163.com'
        password = 'KKNCDTGXBBOUXEBB'

        # 接受邮件的邮箱
        receiver = 'chengp621@163.com'

        # 邮件标题
        subjext = '测试报告'
        # 获取附件信息
        with open(report_name, "rb") as f:
            body = f.read().decode()
        message = MIMEMultipart()

        # 发送地址
        message['from'] = sender
        message['to'] = receiver
        message['subject'] = subjext

        # 正文
        body = MIMEText(body, 'html', 'utf-8')
        message.attach(body)

        # 同一目录下的文件
        att = MIMEText(open(report_name, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'

        # filename附件名称
        att["Content-Disposition"] = 'attachment; filename="result.html"'
        message.attach(att)

        # 登录服务器发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(sender, password)
        smtp.sendmail(sender, receiver, message.as_string())
        smtp.quit()


if __name__ == '__main__':
    name = r'D:\workspace\study\nftgowebtest\report\html\index.html'
    Email().send_email(name)