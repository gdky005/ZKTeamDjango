#暂时不能抽离工具类
# import json
#
# from django.http import HttpResponse
# from dss.Serializer import serializer
# from api.ResultResponse import ResultResponse
#
#
# class HttpResponseUtil:
#
#     def getHttpResponse(self, code, message, word):
#         resultResponse = ResultResponse(code, message, word)
#         return HttpResponse(json.dumps(serializer(resultResponse.__dict__), ensure_ascii=False),
#                             content_type="application/json")
#         # return HttpResponse(data, content_type="application/json")
