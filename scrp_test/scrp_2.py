
import urllib.request,urllib.error
from bs4 import BeautifulSoup

#acess url
url = "https://www.nikkei.com/markets/worldidx/chart/nk225/"
nikkei_heikin = ""


html = urllib.request.urlopen(url)

soup = BeautifulSoup(html,"html.parser")

span = soup.select_one("#MAIN_CONTENTS > div:nth-child(4) > div.m-article.economic > div.economic_value > span.economic_value_now.a-fs26").text

span2 = soup.select_one("body > div:nth-child(9) > div > div > div > div:nth-child(3) > div > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)").text

print(span)
print(span2)
