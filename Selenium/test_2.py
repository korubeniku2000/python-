# Seleniumで操作したURLをBeautifulSoupに
# 読み込ませる。

#====import====================
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request,urllib.error
import time

#====funtion===================

#指定したidの要素に文字を入力する
def input_element_id(driver ,input_id, input_word) :
    id = driver.find_element_by_id(input_id)
    id.send_keys(input_word)
    time.sleep(1)

#指定したnameの要素に文字を入力する
def input_element_name(driver ,input_name, input_word) :
    id = driver.find_element_by_name(input_name)
    id.send_keys(input_word)
    time.sleep(1)

#指定したidの要素をクリックする
def click_element_id(driver ,input_id):
    id = driver.find_element_by_id(input_id)
    id.click()
    time.sleep(1)

def click_element_class(driver ,input_class):
    id = driver.find_element_by_class_name(input_class)
    id.click()
    time.sleep(1)

def click_element_name(driver ,input_name):
    id = driver.find_element_by_name(input_name)
    id.click()
    time.sleep(1)

def click_element_xpath(driver ,input_xpath):
    id = driver.find_element_by_xpath(input_xpath)
    id.click()
    time.sleep(1)

#====main======================

#変数定義
URL = ""
URL2 = ""

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

login_name = ""       #ログインユーザ名
login_pass = ""       #ログインパスワード

#Goorle Chrome起動
driver.get(URL)

#(1)ログイン///////////
#ユーザ名入力
input_element_name(driver,"",login_name)

#パスワード入力
input_element_name(driver,"",login_pass)

#[ログイン]ボタンクリック
click_element_class(driver,"")

driver.get(URL2)

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

print(driver.page_source)
