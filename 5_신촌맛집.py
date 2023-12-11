from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import pyautogui

search_text = pyautogui.prompt('검색어')

driver = webdriver.Chrome()

driver.get('https://map.naver.com/p')

time.sleep(2)

search = driver.find_element(value = '.input_search', by = By.CSS_SELECTOR)

search.send_keys(search_text)
search.send_keys(Keys.ENTER)

time.sleep(1)

driver.switch_to.frame(driver.find_element(value='#searchIframe', by=By.CSS_SELECTOR)) # frame 전환

title_arr = []

#  page까지
for _ in range(3):
    while True:
        scroll_height = driver.execute_script('return document.querySelector("#_pcmap_list_scroll_container").scrollHeight')

        driver.execute_script('document.querySelector("#_pcmap_list_scroll_container").scrollBy(0, document.querySelector("#_pcmap_list_scroll_container").scrollHeight)')

        # 신규 데이터 로딩
        time.sleep(2)
        
        new_scroll_height = driver.execute_script('return document.querySelector("#_pcmap_list_scroll_container").scrollHeight')

        # 만약 새로운 데이터가 없다면
        if scroll_height == new_scroll_height:
            break;

    list = driver.find_elements(value='#_pcmap_list_scroll_container > ul > li', by=By.CSS_SELECTOR)

    for item in list:
        title = item.find_element(value='div.CHC5F > a.tzwk0 > div > div > span.TYaxT', by=By.CSS_SELECTOR).text
        title_arr.append(title)
    
    # 다음 페이지 로딩
    next_button = driver.find_element(value='#app-root > div > div.XUrfU > div.zRM9F > a:nth-child(7)', by=By.CSS_SELECTOR)
    next_button.click()
    time.sleep(2)

df = pd.DataFrame({
    'title': title_arr,
})

df.to_excel('맛집.xlsx')