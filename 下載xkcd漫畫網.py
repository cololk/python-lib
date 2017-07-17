#-*- coding:utf-8 -*-
#本程式可用來下載xkcd漫畫網
import requests, os, bs4
url="http://xkcd.com"
os.makedirs("xkcd", exist_ok=True) #將資料存在./xkcd
while not url.endswith("#"):  #如果url是以"#"做結尾,就結束迴圈(程式用倒述法,不是#結尾就繼續)
	print("Downloading page %s...." % url)
	res=requests.get(url)
	res.raise_for_status() #如果前段下載有問題,就丟出例外
	soup=bs4.BeautifulSoup(res.text,"html.parser")
	comicElem=soup.select("#comic img") #抽取出id為comic的img元素
	if comicElem==[]:
		print("Could not find comic image.")
	else:
		try:
			comicUrl="http:"+comicElem[0].get("src")
			print("Downloading image %s..." % (comicUrl))
			res=requests.get(comicUrl)
			res.raise_for_status()
		except requests.exceptions.MissingSchema:
			prevLink=soup.select('a[rel="prev"]')[0]
			url="http://xkcd.com"+ prevLink.get("href")
			continue
        #os.path.join("a","b")可將a與b加上作業系統的路徑斜線,可依windows(反斜線\)或linux(斜線/)自動調整
		imageFile=open(os.path.join('xkcd', os.path.basename(comicUrl)), "wb")
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()

	prevLink=soup.select('a[rel="prev"]')[0] #選擇器會抽取出rel屬性設定為prev的<a>元素
	url='http://xkcd.com'+prevLink.get('href')
print('Done')
