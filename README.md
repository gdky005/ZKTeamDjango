# ZKTeamDjango


### Django 启动不了？

	这是一个不断试错的过程，不过最终从各种问题中依次解决，推断出问题所在。


	最终是必须在项目的根目录下运行可以成功。其中把环境切换到了 3.6的环境，之前默认是2.7. 3， 3.4 试过好多都不行。

### ubuntu16.04中将python3设置为默认

直接执行这两个命令即可：
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2 100
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 150

如果要切换到Python2，执行：
sudo update-alternatives --config python

根据命令行提示 选择数字回复。


### 添加项目后，本地能运行，服务器无法直接运行？
   可以尝试给服务器的域名后面加上端口号，如果端口号可以，但是直接运行不了，可以修改 Nginx 的配置。














