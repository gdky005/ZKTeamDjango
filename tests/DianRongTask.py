import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_pass = "wq12345678"  # 发件人密码
my_sender = "gdky005@126.com"  # 发件人邮箱账号
my_smtp = "smtp.126.com"  # smtp 地址
my_smtp_port = 25  # smtp 端口号
my_user = "741227905@qq.com"  # 收件人邮箱账号
my_sender_nickname = "ZKTeam 服务器"
my_user_nickname = "孤独狂饮"


def mail(subject, info):
    ret = True

    try:
        msg = MIMEText(info, "plain", 'utf-8')
        msg['From'] = formataddr([my_sender_nickname, my_sender])
        msg['To'] = formataddr([my_user_nickname, my_user])
        msg['Subject'] = subject

        server = smtplib.SMTP(my_smtp, my_smtp_port)
        server.login(my_sender, my_pass)
        server.sendmail(my_sender, [my_user], msg.as_string())
        server.quit()
        print("ok")
    except Exception:
        ret = False
        print("filed")
    return ret


# ret = mail("test 主题", "主题内容")
# if ret:
#     print("ok")
# else:
#     print("filed")
