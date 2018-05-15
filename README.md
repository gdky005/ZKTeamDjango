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


### 创建一个项目
1. 创建项目命令：
```
    python manage.py startapp app_name
```
2. 在项目目录下创建 templates 文件夹，可以放很多的 html 和图片等资源文件, 创建默认文件：
```
    xxx_index.html
```
3. 在 models.py 文件里面添加 该 app 的 数据库需要的字段。例如：
```
    # Create your models here.

    class xxx(models.Model):
        id = models.IntegerField(primary_key=True).auto_created
        jid = models.IntegerField()
        name = models.TextField()
        url = models.TextField()
    ```
4. 创建 urls.py 文件，配置当前 module 的 url 路径
```
    urlpatterns = [
        url(r'^index.html',  views.XXX, name="XXX"),
    ]
```

在 ZKTeam 目录下面的 urls.py 里面添加：
```
url(r'^XXX/', include('XXX.urls', namespace='XXX', app_name='XXX')),
```

5. 在 views.py 里面添加通用代码：
```
    import json
    from django.http import HttpResponse
    from django.shortcuts import render

    from dss.Serializer import serializer
    from pymysql import Error

    from api.ResultResponse import ResultResponse


    def xxx(request):
        projects = models.xxx.objects.all()
        return render(request, 'XXX', {"projects": projects})


    def xxx(request):
        maxData = 5
        count = request.GET.get("pageCount")
        if count:
            maxData = int(count)

        try:
            # projects = models.xxx.objects.all()

            project_info = models.xxx.objects.values()[:maxData]  # 取出该表所有的数据
            projects = list(project_info)

            return getHttpResponse(0, "ok", projects)
        except Error:
            return getHttpResponse(10000, "Error", "")


    def getHttpResponse(code, message, word):
        resultResponse = ResultResponse(code, message, word)
        return HttpResponse(json.dumps(serializer(resultResponse.__dict__), ensure_ascii=False, ),
                            content_type="application/json;charset=utf-8")

    ```



6. 在 ZKTeam 目录下面的 settings.py 的 INSTALLED_APPS 里面加入 XXX ,当前 module 的名称

7. 将项目中确实的数据填写完成即可。
8. 同步数据库：
```
# 1. 创建更改的文件
python manage.py makemigrations
# 2. 将生成的py文件应用到数据库
python manage.py migrate
```
8. 本地调试：
```
python manage.py runserver
```
9. 在网页里面输入：
```
http://127.0.0.1:8000/XXX/index.html
```

### 添加缓存
http://django-redis-chs.readthedocs.io/zh_CN/latest/

