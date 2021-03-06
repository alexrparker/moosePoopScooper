from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import datetime
import time
import os
from pytz import timezone
import gc

song_data_old = ''
url='http://radioplayer.vistaradio.ca/chms/'

ts = time.time()
EST = timezone('America/New_York')
start_time = datetime.datetime.now(tz=EST).strftime('%Y-%m-%d %H:%M:%S')
csvStart=["Program launched", start_time]

with open(r'document.csv', 'a') as f:
  writer = csv.writer(f)
  writer.writerow(csvStart)
  

while True:
  ts1 = datetime.datetime.now(tz=EST).strftime('%Y-%m-%d %H:%M:%S')

  os.system('pkill chrome')
  time.sleep(2)
  from selenium import webdriver
  from bs4 import BeautifulSoup

  
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--no-sandbox') # required when running as root user. otherwise you would get no sandbox errors. 
  chrome_options.add_argument('--incognito')
  chrome_options.add_argument("--disable-setuid-sandbox")
  #chrome_options.add_argument("start-maximized")
  
  try:
    driver = webdriver.Chrome(chrome_options=chrome_options,service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])
  except:
    print ("Exception! = webdriver \n")
    continue
  
  try:
    driver.get(url) 
  except:
    print ("Exception! driver.get(url) \n")
    continue
  

 
  #print(driver.title)
  try:
    page_data = driver.page_source
  except:
    print ("Exception! page_data = driver.page_source \n")
    continue
  
  
  #song = driver.find_element_by_xpath('//*[@id="live-strip"]/div[3]/div/div/div[1]/span')
  soup_data = BeautifulSoup(page_data, features="html5lib")

  
  #for link in page_data.find_all('span'):
  #    print link.get('span',None),link.get_text()
      
  song_data = soup_data.find('span', {'class' : 'song-text'})
  
  #driver.close()
  #os.system('pkill chrome')
  
  myCsvRow=[song_data, ts1]
  print(myCsvRow) 
  
  if song_data == song_data_old:
    print('Same old song \n')
  #elif song_data.find('Bancroft')  is not -1:
  #  print('Commercials \n')
  else:
    with open(r'document.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(myCsvRow)
        print("New Song! Writin' it to the file. \n")
    song_data_old = song_data
  
  gc.collect()
  time.sleep(60)
    
  #END OF LOOP
  

    
