import requests
from bs4 import BeautifulSoup
payload={"from":"/bbs/Gossiping/index.html", "yes":"yes"}
rs=requests.session() #由於ptt要先經過18歲認證頁面才會進入主頁,所以須透過session才能記錄這樣的先後動作
res=rs.post("https://www.ptt.cc/ask/over18", verify=False, data=payload)
res=rs.get("https://www.ptt.cc/bbs/Gossiping/index.html", verify=False)
soup=BeautifulSoup(res.text,"html.parser")
content=soup.select(".r-ent")
for entry in content:
	print(entry.select(".title")[0].text, entry.select(".date")[0].text, entry.select(".author")[0].text)