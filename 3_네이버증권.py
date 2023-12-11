from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

#상세페이지 주소
response = urlopen('https://finance.naver.com/')

#상세페이지 전체 text 
text = response.read()

#text parsing
soup = BeautifulSoup(text, 'html.parser', from_encoding='cp949')

#하나만 고르는 경우 nth-child, 복수개일땐 아님
rows = soup.select('#_topItems1 > tr')

name_list = []
total_value_list = []
change_value_list = []
percentage_list = []

for row in rows:
    name = row.select_one('th').text
    total_value = row.select_one('td:nth-child(2)').text
    change_value = row.select_one('td:nth-child(3)').text
    percentage = row.select_one('td:nth-child(4)').text

    name_list.append(name)
    total_value_list.append(total_value)
    change_value_list.append(change_value)
    percentage_list.append(percentage)

df = pd.DataFrame({
    '종목명': name_list,
    '시가총액': total_value_list,
    '변동액': change_value_list,
    '변동률': percentage_list,
})

df.to_excel('주식.xlsx')