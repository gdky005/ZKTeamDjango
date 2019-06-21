import xadmin

# Register your models here.
from ManHua.models import Category, MHDetail, MHDetailChapter, MHChapterPic, MHBanner, CategoryForCategoryId, HotData, \
    SelectData, MHAllData

xadmin.site.register(Category)
xadmin.site.register(HotData)
xadmin.site.register(SelectData)
xadmin.site.register(MHDetail)
xadmin.site.register(MHDetailChapter)
xadmin.site.register(MHChapterPic, MHChapterPic.ShowXItem)
xadmin.site.register(MHBanner)
xadmin.site.register(CategoryForCategoryId)
xadmin.site.register(MHAllData)

