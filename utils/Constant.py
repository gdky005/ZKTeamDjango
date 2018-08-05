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
    wx_access_token = "12_fwlvrLgCjUrF2T1lXn440IJhmZ7actxoYLubKZH6KVuhtG631xpEQCntyC7E-rCggN_TUlZsNsUuMgTjrwyT8m6n4-6FsX2M-HNuPKQPUs5KKWA3Ubuy2RG8jhrcJiAWxY39zGGdG7yj3Hc8PNWiADASQZ"
    expires_in = ""
    refresh_time = ""



print(Constant.my_user_nickname)