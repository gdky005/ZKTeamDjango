import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

from utils.Constant import Constant


def send(subject, info):
    return send(subject, info, None, None)


def send(subject, info, userEmail, userName):
    my_pass = Constant.secret_126
    my_sender = Constant.my_sender  # 发件人邮箱账号
    my_smtp = Constant.my_smtp  # smtp 地址
    my_smtp_port = Constant.my_smtp_port  # smtp 端口号
    my_user = Constant.my_user  # 收件人邮箱账号
    my_sender_nickname = Constant.my_sender_nickname
    my_user_nickname = Constant.my_user_nickname

    if userEmail:
        my_user = userEmail
    else:
        my_user_nickname = userName

    # response = {"sendType": "Email", "sendUser": sendUser, "sendUserName": sendUserName}
    response = {}

    if my_pass.__eq__(""):
        ret = False
        error = "filed， 请输入邮件发送人的密码，谢谢！（在项目根目录下配置 zk_local_secret.gdky005 文件）"
        response["exception"] = error
        return response

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

        response["SendState"] = "OK!"
    except Exception as e:
        errorStr = str(e)
        print("filed:" + errorStr)
        response["exception"] = errorStr

    return response
