from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

#요청 - 응답
response = urlopen('https://www.mk.co.kr/')

text = response.read()

#parsing
soup = BeautifulSoup(text, 'html.parser')

#복사한 selector 입력
headline_1 = soup.select_one('#headline_1')
headline_1_text = headline_1.text.strip()

headline_1_1 = soup.select_one('#container > section > div.mk_head_news_group > div > div > div.col.main_col > section > div > ul > li.col.col_12.news_node.headline_news_node > div > div > ul > li:nth-child(1) > a')
headline_1_1_text = headline_1_1.text.strip()

headline_1_2 = soup.select_one('#container > section > div.mk_head_news_group > div > div > div.col.main_col > section > div > ul > li.col.col_12.news_node.headline_news_node > div > div > ul > li:nth-child(2) > a')
headline_1_2_text =headline_1_2.text.strip()

print(headline_1_1_text)
print(headline_1_2_text)

df = pd.DataFrame({
    '본문' : [headline_1_text, headline_1_1_text, headline_1_2_text]
})

df.to_excel('매일경제.xlsx')