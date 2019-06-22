import json

from django.shortcuts import render
from django.views.decorators.cache import cache_page

from ManHua import models
from ManHua.Utils import getHashCode
from ManHua.base_views import getPagingData, getHttpTotalResponse, getHttpResponse, getPagingDataForFilter
from ManHua.models import Category, HotData, MHDetail, MHDetailChapter, MHChapterPic, MHBanner, SelectData, MHAllData
from pymysql import Error


@cache_page(60 * 5)
def JsonMHAllDataView(request):
    return getPagingData(request, MHAllData)


@cache_page(60 * 15)  # 秒数，这里指缓存 15 分钟，不直接写900是为了提高可读性
def JsonMHCategoryView(request):
    print("开始读取 分类 数据")
    return getPagingData(request, Category)


@cache_page(60 * 5)
def JsonMHHotDataView(request):
    return getPagingData(request, HotData)


@cache_page(60 * 5)
def JsonMHSelectDataView(request):
    return getPagingData(request, SelectData)


@cache_page(60 * 5)
def JsonMHDetailView(request):
    mid = request.GET.get("mid")

    if mid is not None:
        obj = models.MHDetail.objects.filter(mid=mid).values()[0]
        return getHttpResponse(0, "ok", obj)
    else:
        return getErrorResponse()


@cache_page(60 * 5)
def JsonMHDetailChapterView(request):
    mid = request.GET.get("mid")

    if mid is not None:
        obj = models.MHDetailChapter.objects.filter(mid=mid).values()
        return getPagingDataForFilter(request, obj)
    else:
        return getErrorResponse()


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
            numPicUrl = picUrl[picUrl.rindex('/') + 1:picUrl.rindex('.')]

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
            return getErrorResponse()
    except Error:
        return getHttpResponse(10000, "Error", "")
    except Exception as e:
        return getHttpResponse(10000, "Error", e)


@cache_page(60 * 5)
def JsonMHBannerView(request):
    return getPagingData(request, MHBanner)


@cache_page(60 * 5)
def JsonMHCategoryForCategoryIdView(request):
    try:
        # 根据漫画的分类 id，获取当前分类下的所有 漫画信息。
        id = request.GET.get("id")
        mid = request.GET.get("mid")

        if mid is not None:
            mid = models.Category.objects.filter(mid=mid)[0].id
        else:
            mid = id

        if mid is not None:
            # categoryId = models.Category.objects.filter(mid=cid)[0].id
            chapterPic = models.CategoryForCategoryId.objects.filter(cid_id=mid)
            obj = []

            for chapter in chapterPic:
                obj.append(chapter.mid)

            return getHttpTotalResponse(0, "ok", chapterPic.count(), obj)
        else:
            return getErrorResponse()
    except Error:
        return getHttpResponse(10000, "Error", "")
    except Exception as e:
        return getHttpResponse(10000, "Error", e)


def getErrorResponse():
    return getHttpResponse(10000, "请在接口扣添加参数：mid", {})


def setMHDetailView(request):
    try:
        errorMsg = ""
        if request.method == 'POST':
            try:
                postBody = request.body
                resultListData = json.loads(postBody)
                # print(result)

                detail_list = []
                for result in resultListData:
                    name = result['name']
                    remind = result['remind']
                    picUrl = result['picUrl']

                    detail = result['detail'].strip()

                    time = result['time']
                    if "：" in time:
                        time = time[time.index("：") + 1:]

                    state = result['state']
                    stateId = getHashCode(state)

                    author = result['author']
                    if "：" in time:
                        author = author[author.index("：") + 1:]

                    url = result['url']
                    if url[len(url) - 1] == "/":
                        mid = url[url.index("com/") + 4:url.rindex("/")]  # 'zhenhunjie'
                        # urlMid = url[url.index("com/") + 4:url.rindex("/")] #'zhenhunjie'
                    else:
                        mid = url[url.index("com/") + 4:]  # 'zhenhunjie'
                    mid = getHashCode(mid)

                    category = result['category']
                    category = category.split(",")
                    categoryIdList = []
                    for item in category:
                        categoryId = getHashCode(item)
                        print(item + "->" + str(categoryId))
                        categoryIdList.append(categoryId)

                    tag = result['tag']

                    mhDetail = MHDetail()
                    mhDetail.name = name
                    mhDetail.remind = remind
                    mhDetail.picUrl = picUrl
                    mhDetail.detail = detail
                    mhDetail.time = time
                    mhDetail.state = state
                    mhDetail.stateId = stateId
                    mhDetail.author = author
                    mhDetail.url = url
                    mhDetail.mid = mid
                    mhDetail.category = category
                    mhDetail.categoryIdList = categoryIdList
                    mhDetail.tag = tag

                    # obj = mhDetail.save()
                    detail_list.append(mhDetail)

                models.MHDetail.objects.bulk_create(detail_list)

                return getHttpResponse(0, "ok", {})

            except Exception as e:
                print(e)
            errorMsg = e
        else:
            errorMsg = "not is post."
        return getHttpResponse(10001, errorMsg, {})
    except Error:
        return getHttpResponse(10000, "Error", "")
    except Exception as e:
        return getHttpResponse(10000, "Error", e)


def setJsonMHChapterData(request):
    try:
        errorMsg = ""
        if request.method == 'POST':
            try:
                postBody = request.body
                resultListData = json.loads(postBody)
                # print(result)

                detail_list = []
                for result in resultListData:

                    name = result['name']
                    pCount = result['pCount']
                    url = result['url']

                    urlSource = url[url.index("com/") + 4:url.rindex("/")]
                    mid = getHashCode(urlSource)

                    count = pCount[pCount.index("（") + 1:pCount.index("P")]

                    mhDetailChapter = MHDetailChapter()
                    mhDetailChapter.name = name
                    mhDetailChapter.mid = mid
                    mhDetailChapter.url = url
                    mhDetailChapter.pCount = pCount
                    mhDetailChapter.count = count

                    # obj = mhDetail.save()
                    detail_list.append(mhDetailChapter)

                models.MHDetailChapter.objects.bulk_create(detail_list)

                return getHttpResponse(0, "ok", {})

            except Exception as e:
                print(e)
            errorMsg = e
        else:
            errorMsg = "not is post."
        return getHttpResponse(10001, errorMsg, {})
    except Error:
        return getHttpResponse(10000, "Error", "")
    except Exception as e:
        return getHttpResponse(10000, "Error", e)

