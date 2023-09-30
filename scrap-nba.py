import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
import json

# Preparar conteúdo HTML a partir da URL
url = 'https://stats.nba.com/players/traditional/?PerMode=Totals&Season=2019-20&SeasonType=Regular%20Season&sort=PLAYER_NAME&dir=-1'
binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')

option = Options()
option.headless = True
driver = webdriver.Firefox(firefox_binary=binary, executable_path='C:\\geckodriver.exe')

driver.get(url)
#time.sleep(10)


# Manipulando p conteúdo da página HTML
#driver.find_element_by_xpath(
#    "//div[@class='Crom_table__p1iZz']//table//thead//tr//th[@field='PTS']").click()
#time.sleep(10)

#driver.find_element("xpath","//div[@class='Crom_table__p1iZz']//table//thead//tr//th[@field='PTS']").click()


#element = driver.find_element_by_xpath("//div[@class='nba-stat-table']//table")
element = driver.find_element(By.XPATH, "//*[@class='Crom_table__p1iZz']")
html_content = element.get_attribute('outerHTML')
print(html_content)
time.sleep(5)

# Parsear conteúdo HTML - BeautifulSoup
soup = BeautifulSoup(html_content, 'lxml')
table = soup.find(name='table')
print(table)

# Estrurar conteúdo em um Data Frame - Pandas
df_full = pd.read_html(str(table))
print(df_full)

driver.quit()

# Transdormar o dados em um dicionário 
# Converter par a JSON 

