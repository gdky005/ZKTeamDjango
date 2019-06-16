import xadmin

# Register your models here.
from ManHua.models import Category, MHDetail, MHDetailChapter, MHChapterPic, MHBanner, CategoryForCategoryId

xadmin.site.register(Category)
xadmin.site.register(MHDetail)
xadmin.site.register(MHDetailChapter)
xadmin.site.register(MHChapterPic, MHChapterPic.ShowXItem)
xadmin.site.register(MHBanner)
xadmin.site.register(CategoryForCategoryId)

