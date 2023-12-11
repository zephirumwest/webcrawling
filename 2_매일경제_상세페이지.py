from urllib.request import urlopen
from bs4 import BeautifulSoup
#상세페이지 주소
response = urlopen('https://www.mk.co.kr/news/economy/10886649')

#상세페이지 전체 text 
text = response.read()

#text parsing
soup = BeautifulSoup(text, 'html.parser')

body = soup.select_one('#container > section > div.news_detail_body_group > section > div.min_inner > div.sec_body > div.news_cnt_detail_wrap')
body_text = body.text.strip()

print(body_text)