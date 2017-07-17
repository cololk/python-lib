#-*- coding:utf-8 -*-
#本程式可用命令列來開啟Google搜尋內容
#目前此程式無法正常運作, 發現主要原因為soup選出的標籤不在res中
#可能原因為網頁有用到javascript生成程式碼
import requests, sys, webbrowser, bs4
from selenium import webdriver

browser=webdriver.Firefox()
browser.get("http://www.google.com.tw")

print ("Googleing...")
#print(sys.argv[1:])
res= requests.get("http://google.com.tw/#q=programming")
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text,"html.parser")
linkElems=soup.select('.r a') #找出所有具有r類別的<a>元素
numOpen=min(5, len(linkElems))
for i in range(numOpen):
	browser.open("http://google.com"+linkElems[i].get('href'))
