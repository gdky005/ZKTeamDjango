import configparser


class Constant:
    config = configparser.ConfigParser()
    config.read("./zk_local_secret.gdky005")
    secret_126 = config.get("global", "secret_126")
    my_sender = config.get("global", "my_sender")
    my_smtp = config.get("global", "my_smtp")
    my_smtp_port = config.get("global", "my_smtp_port")
    my_user = config.get("global", "my_user")
    my_user_nickname = config.get("global", "my_user_nickname")
    my_sender_nickname = config.get("global", "my_sender_nickname")


class WXConstant:
    # 默认值，刷新成功后，会替换
    wx_access_token = "12_433alEqCy2ajGVYkxndBWsWdpliuVIimiFxP24c7R7MgWie2XY-00CPIqHaExXsimU3Lm8OfNUcj4ndMIzr83pzY_Jk-pGvMZ9P3RUwfrqnRjEbh3ueU9H5ZOXhWOwaOwahnX6rMEvk-fJJMSIYgAAAKAQ"
    expires_in = ""
    refresh_time = 0



print(Constant.my_user_nickname)