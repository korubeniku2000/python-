#Selniumを使用したyahooメールログイン

#====import====================
from selenium import webdriver
import time

#====funtion===================

#指定したidの要素に文字を入力する
def input_element_id(driver ,input_id, input_word) :
    id = driver.find_element_by_id(input_id)
    id.send_keys(input_word)
    time.sleep(1)

#指定したidの要素をクリックする
def click_element_id(driver ,input_id):
    id = driver.find_element_by_id(input_id)
    id.click()
    time.sleep(1)

#====main======================

#変数定義
URL = "https://login.yahoo.co.jp/config/login?.src=ym&.done=https%3A%2F%2Fmail.yahoo.co.jp%2F"
driver = webdriver.Chrome("/usr/local/bin/chromedriver")

login_name = ""       #ログインユーザ名
login_pass = ""       #ログインパスワード

#Goorle Chrome起動
driver.get(URL)

#ユーザ名入力
input_element_id(driver,"username",login_name)

#[次へ]ボタンクリック
click_element_id(driver,"btnNext")


#パスワード入力
input_element_id(driver,"passwd",login_pass)

#[ログイン]ボタンクリック
click_element_id(driver,"btnSubmit")
