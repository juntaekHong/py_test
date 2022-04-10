from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


#브라우저 생성
browser=webdriver.Chrome('C:/chromedriver.exe')

#웹사이트 열기
browser.get('https://www.naver.com')
browser.implicitly_wait(10)#로딩이 끝날때까지 10초까지는 기다려줌


#쇼핑 메뉴 클릭
 
browser.find_element_by_css_selector('a.nav.shop').click()
time.sleep(2)

#검색창 클릭
search=browser.find_element_by_css_selector('input.co_srh_input._input')
search.click()

#검색어를 입력
search.send_keys('아이폰13')
search.send_keys(Keys.ENTER)

#스크롤 전 높이 #execute_script는 자바스크립트를 파이썬안에서 실행시켜주는 명령어
before_h=browser.execute_script('return window.scrollY')


#무한 스크롤
while True:
    # 맨아래로 스크롤을 내린다.
    browser.find_element_by_css_selector("body").send_keys(Keys.END)
    
    #스크롤 사이 페이지 로딩 시간
    time.sleep(2)
    
    #스크롤 후 높이
    after_h =browser.execute_script("return window.scrollY")
    
    if after_h ==before_h:
        break
    before_h =after_h
    
#상품정보 div
items =browser.find_elements_by_css_selector(".basicList_info_area__17Xyo")

for item in items:
    name =item.find_element_by_css_selector(".basicList_title__3P9Q7").text
    try:
        price = item.find_element_by_css_selector(".price_num__2WUXn").text
    except:
        price='판매중단'
    link=item.find_element_by_css_selector("basicList_title__3P9Q7 > a").get_attribute('href')
    print(name,price,link)