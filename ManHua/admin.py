from django.contrib import admin

# Register your models here.
from ManHua.models import Category, MHDetail, MHDetailChapter, MHChapterPic

admin.site.register(Category)
admin.site.register(MHDetail)
admin.site.register(MHDetailChapter)
admin.site.register(MHChapterPic, MHChapterPic.ShowItem)
