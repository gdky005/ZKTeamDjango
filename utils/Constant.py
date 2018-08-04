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
    wx_access_token = "12_yxfKsCz9lGIKiU5B4ovGoEWt5Gx1FchLws7rsZskpWcEUEBaI1HD_X0EEh9LFkgN57pinpz-dCU8gwQAbIW9kT9XgpG1uVANn-5Venaz7Coy9Z7hZcjSdQT4oKAh30Ya0YHbfGKakS7jIW_lEZVeAAAUPL"
    expires_in = ""
    refresh_time = ""



print(Constant.my_user_nickname)