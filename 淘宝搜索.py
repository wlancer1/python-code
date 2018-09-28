import requests
import re
def getHTml(url):
	try:
		r=requests.get(url,timeout=30)
		r.raise_for_status() 
		r.encoding=r.apparent_encoding
		return r.text
	except:
		return "产生异常"

def parsepage(ilt,html):
	try:
		plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
		tlt=re.findall(r'\"raw_title\"\:\".*?\"', html)
		for i in range(len(plt)):
			price=eval(plt[i].split(':')[1])##eval函数去掉引号
			titl=eval(tlt[i].split(':')[1])
			ilt.append([price,titl])
	except:
		print("异常")

def printGoodsList(ilt):
	tplt="{:4}\t{:8}\t{:16}"
	print(tplt.format("id","商品名称","价格"))
	count=0
	for x in ilt:
		count=count+1
		print(tplt.format(count,x[1],x[0]))
def main():
	goods='pixel'
	depth=2
	start_url='https://s.taobao.com/search?q='+goods
	infolist=[]
	for i in range(depth):##如果有页面解析不了跳过，不弹出错误信息
		try:
			url=start_url+'&s='+str(44*i)
			html=getHTml(url)
			parsepage(infolist,html)
		except:
			continue
	printGoodsList(infolist)
if __name__ == '__main__':
	main()