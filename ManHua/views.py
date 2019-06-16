from django.shortcuts import render
from django.views.decorators.cache import cache_page

from ManHua import models
from ManHua.base_views import getPagingData, getHttpTotalResponse, getHttpResponse
from ManHua.models import Category, HotData, MHDetail, MHDetailChapter, MHChapterPic, MHBanner
from pymysql import Error


@cache_page(60 * 15)  # 秒数，这里指缓存 15 分钟，不直接写900是为了提高可读性
def ManHuaIndex(request):
    projects = models.ManHua.objects.all()
    return render(request, 'manhua_index.html', {"projects": projects})


@cache_page(60 * 5)
def JsonMHCategoryView(request):
    print("开始读取 分类 数据")
    return getPagingData(request, Category)


@cache_page(60 * 5)
def JsonMHHotDataView(request):
    return getPagingData(request, HotData)


@cache_page(60 * 5)
def JsonMHDetailView(request):
    return getPagingData(request, MHDetail)


@cache_page(60 * 5)
def JsonMHDetailChapterView(request):
    return getPagingData(request, MHDetailChapter)


@cache_page(60 * 5)
def JsonMHChapterPicView(request):
    try:
        # 根据漫画 id 把漫画具体的 漫画对象拿出来。拼装好以后发给客户端。
        mid = request.GET.get("mid")

        if mid is not None:
            chapterPic = models.MHChapterPic.objects.filter(mid2=mid)[0]
            # chapterPic
            count = chapterPic.count
            picUrl = chapterPic.picUrl
            prePicUrl = picUrl[0:picUrl.rindex('/') + 1]
            sufPicUrl = picUrl[picUrl.rindex('.'):len(picUrl)]
            numPicUrl = picUrl[picUrl.rindex('/')+1:picUrl.rindex('.')]

            # 'https://mh3.xitangwenhua.com/upload/zhegedashutailengao/5312480/0000.jpg'

            pics = []
            numberLength = numPicUrl.__len__()
            for num in range(0, count + 1):
                number = str(num).__len__()
                numStr = str(num)

                diffNum = numberLength - number

                if diffNum == 1:
                    mhNum = "0" + numStr
                elif diffNum == 2:
                    mhNum = "00" + numStr
                elif diffNum == 3:
                    mhNum = "000" + numStr
                elif diffNum == 4:
                    mhNum = "0000" + numStr

                pics.append(prePicUrl + mhNum + sufPicUrl)

            chapterPicObj = {}
            chapterPicObj['id'] = chapterPic.id
            chapterPicObj['mid'] = chapterPic.mid
            chapterPicObj['mid2'] = chapterPic.mid2
            chapterPicObj['picUrl'] = pics
            chapterPicObj['count'] = chapterPic.count
            chapterPicObj['sourceUrl'] = chapterPic.sourceUrl

            return getHttpTotalResponse(0, "ok", count, chapterPicObj)
        else:
            return getHttpResponse(10000, "Error", "请在接口中添加漫画 mid")
    except Error:
        return getHttpResponse(10000, "Error", "")
    except Exception as e:
        return getHttpResponse(10000, "Error", e)


@cache_page(60 * 5)
def JsonMHBannerView(request):
    return getPagingData(request, MHBanner)
