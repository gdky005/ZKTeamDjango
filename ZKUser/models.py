from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class ZKUser(AbstractUser):
    # 继承AbstractUser类，实际上django的User也是继承他，我们要做的就是用自己的类代替django自己的User
    nickname = models.CharField(max_length=200, null=True, blank=True, verbose_name="姓名")
    birthday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(("male", u'男'), ("female", u'女')), default='female')
    address = models.CharField(max_length=11, verbose_name=u'地址', null=True, blank=True)
    # image = models.ImageField(upload_to='image/%Y/%m', default=u"image/default.png", max_length=100)
    phone = models.CharField(max_length=11, verbose_name=u"手机号码", null=True, blank=True)

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username

