import requests as rq
import time
def getHTMLText(url):
    try:
        r=rq.get(url,timeout=30)
        r.raise_for_status() 
        r.encoding=r.apparent_encoding
    except:
        return "产生异常"
url="http://www.baidu.com"
start=time.time()
for i in range(100):
    getHTMLText(url)
end=time.time()
print("爬取100次用时：%fs"%(end-start))