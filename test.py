from selenium import webdriver
import time

driver = webdriver.Chrome('C:/Users/YunTaek/Downloads/chromedriver_win32/chromedriver.exe')
driver.get('https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId=103&date=20190526')
data = []
time.sleep(2)

titles = driver.find_elements_by_css_selector('div.ranking_headline a')
url_list = []

for title in titles:
    url_list.append(title.get_attribute('href'))


for i in range(len(url_list)):
    dic = {}
    comment_list = []
    driver.get(url_list[i])
    time.sleep(0.5)
    comments = driver.find_elements_by_css_selector('span.u_cbox_contents')
    
    for comment in comments:
        comment_list.append(comment.text)

    dic["title"] = title_list[i]
    dic["url"] = url_list[i]
    dic["comment"] = comment_list
    comment_list = []

    print(dic)

    data.append(dic)