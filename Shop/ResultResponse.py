class ResultResponse(object):

    def __init__(self, code, message, result):
        self.code = code
        self.message = message
        self.result = result

    def __str__(self):
        return '{"code":%s,"message":%s,"result":%s}' % (self.code, self.message, self.result)

    # @property
    # def code(self):
    #     return self.code
    #
    # @code.setter
    # def code(self, code):
    #     self.code = code
    #
    # @property
    # def message(self):
    #     return self.message
    #
    # @message.setter
    # def message(self, message):
    #     self.message = message
    #
    # @property
    # def result(self):
    #     return self.result
    #
    # @result.setter
    # def result(self, result):
    #     self.result = result

#     def __str__(self):
#         return '%s,%s,%s' % (self.code, self.message, self.result)
#
# t = ResultResponse(0, "ok", "test")
# t.code = 200
# t.message = "hello"
# t.result = "data"
# print(t)


    # resultResponse = ResultResponse(0, "ok", data)
    # resultResponse.code(0)
    # resultResponse.message("ok")
    # resultResponse.result(data)