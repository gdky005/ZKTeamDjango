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


print(Constant.my_user_nickname)