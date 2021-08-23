from time import sleep, strftime
from random import randint
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
from email.mime.multipart import MIMEMultipart

chromedriver_path = './usr/local/bin/chromedrive'

driver = webdriver.Chrome()
sleep(2)

NanHang = "https://b2c.csair.com/ita/newIntl/zh/shop/?execution=fe519ebe7d9668271552edf09b9de697"
driver.get(NanHang)
sleep(3)