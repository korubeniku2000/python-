
##試験用
##実施は自己責任でお願いします。

import urllib.request,urllib.error
from bs4 import BeautifulSoup

#acess url
url = "https://job.inshokuten.com/kanto/work/?mode=index&searchRegionArea=tokyo_all&indexLink=1"

html = urllib.request.urlopen(url)

soup = BeautifulSoup(html,"html.parser")

cls = soup.find_all("article")


for cl in cls:
    div = cl.find("div",class_="catch-phrase")
    a = div.find("a")
    word = a.get_text()
    print(word.strip())
