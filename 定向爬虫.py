import requests
from bs4 import BeautifulSoup
import bs4
#获取html文本
def getHtmltext(url):

	try:
		r=requests.get(url)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text
	except :
		return ""
##将数据放入ullist
def fillulist(ulist,html):
	soup = BeautifulSoup(html, "html.parser")
	for tr in soup.find('tbody').children:
		if isinstance(tr, bs4.element.Tag):
			print(tr.td.prettify().split('\n')[1])
			tds = tr('td')
			ulist.append([tds[0].string, tds[1].string, tds[3].string])

			##输出ulist信息
def printUlist(ulist,num):
	print("{}\t{}\t{}".format("排名","学校名称","学校总分"))
	for i in range(num):
		u=ulist[i]
		print(u)
		print("{}\t{}\t{}".format(u[0],u[1],u[2]))
	pass
def main():
	uinfo=[] 
	url='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html'
	html=getHtmltext(url)
	fillulist(uinfo,html)
	pass
main()