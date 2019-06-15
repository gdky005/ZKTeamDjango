import xadmin

# Register your models here.
from ManHua.models import Category, MHDetail, MHDetailChapter, MHChapterPic

xadmin.site.register(Category)
xadmin.site.register(MHDetail)
xadmin.site.register(MHDetailChapter)
xadmin.site.register(MHChapterPic, MHChapterPic.ShowXItem)

