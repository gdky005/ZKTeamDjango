from django.test import TestCase

# 这是单元测试
# Create your tests here.
class TestDB(TestCase):

    def test_db1(self):
        from api import models
        user_list = models.UserInfo.objects.all()
        print(user_list.count())
