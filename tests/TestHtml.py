from bs4 import BeautifulSoup
import requests
import json
from utils import Email

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML," \
             " like Gecko) Chrome/19.0.1084.54 Safari/536.5"

# url = "https://www.dianrong.com/market"
url = "https://www.dianrong.com/feapi/plans"

headers = {"Accept": "text/html,application/xhtml+xml,application/xml;",
           "Accept-Encoding": "gzip",
           "Accept-Language": "zh-CN,zh;q=0.8",
           "User-Agent": user_agent
           }

response = requests.get(url, headers=headers)


jsonData = response.json()
xrbData = jsonData.get("content").get("list")[1]
jjfData = jsonData.get("content").get("list")[4]

xrb = xrbData.get("name"), "_开放额度:", xrbData.get("openAmount")
jjf = jjfData.get("name"), "_开放额度：", jjfData.get("openAmount")

print(xrb)
print(jjf)


totalContent = xrb.__str__() + "\n\n" + jjf.__str__()

# jjfIntData = jjfData.get("openAmount") == 0
jjfIntData = jjfData.get("openAmount") > 100

jjfSub = "季季翻      【未开启】"
if jjfIntData:
    jjfSub = "季季翻      已经开启啦!"
    Email.send(jjfSub, totalContent.__str__())
print(jjfSub)





# data = json.dumps(jsonData)
# print(data)



# print(json.dumps(response.text, sort_keys=True,ensure_ascii=False))

# htmlContent = response.content.decode("utf8", response.text)
# print(htmlContent.json)

# soup = BeautifulSoup(htmlContent, "lxml")
# # print(soup.prettify())
# # print(soup.p)
# # print(soup.div['sl-plan-card ng-isolate-scope'])
#
# # print soup.find_all('a')
# # print(soup.find_all("div"))
# # soup.select('a[class="sister"]')
#
# # [class="sl-plan-card ng-isolate-scope"]
# print(soup.select('div[class="sl-plan-card ng-isolate-scope"]'))