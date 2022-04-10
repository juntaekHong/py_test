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