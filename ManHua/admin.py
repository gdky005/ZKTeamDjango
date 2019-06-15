from django.contrib import admin

# Register your models here.
from ManHua.models import Category, MHDetail, MHDetailChapter, MHChapterPic

admin.site.register(Category, Category.ShowItem)
admin.site.register(MHDetail, MHDetail.ShowItem)
admin.site.register(MHDetailChapter, MHDetailChapter.ShowItem)
admin.site.register(MHChapterPic, MHChapterPic.ShowItem)
