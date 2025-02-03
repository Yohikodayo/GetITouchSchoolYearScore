from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


# click element -> element.click()
# input text -> element.send_keys()
# get text -> element.text
# get attribute -> element.get_attribute()
# get css value -> element.value_of_css_property()
# get tag name -> element.tag_name
# find element -> driver.find_element(By.CSS_SELECTOR, "selector")
# close driver -> driver.quit()


# 初始化瀏覽器
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")  # 避免權限問題
options.add_argument("--disable-dev-shm-usage")  # 增加對大數據的支援
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = "https://itouch.cycu.edu.tw/home/#/ann"
driver.get(url)

time.sleep(1)

# todo 進行操作
id_input_ele = driver.find_elements(By.CSS_SELECTOR, "[name='UserNm']")
pwd_input_ele = driver.find_elements(By.CSS_SELECTOR, "[name='UserPasswd']")

st_id = input("請輸入學號: ")
st_pwd = input("請輸入密碼: ")

if not st_id or not st_pwd:
    print("請輸入學號和密碼")
    exit()

id_input_ele[0].send_keys(st_id)
pwd_input_ele[0].send_keys(st_pwd)

time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "[name='Submit']").click()

# * 檢查是否有帳號或密碼錯誤的alert
# if len(driver.find_elements(By.CSS_SELECTOR, "")) > 0:
#     pass

time.sleep(3)

# * 檢查是否有修改密碼的alert
if len(driver.find_elements(By.CSS_SELECTOR, "")) > 0:
    pass


# * 點擊歷年成績的連結

