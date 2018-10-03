# moosePoopScooper
This is a webscraper written in python, used to scrape song titles and the time they played from a javascript HTML source into a csv list. 

Seems to work well enough inside a c9 python environment. 

This site was very helpful with the setup. Although, I had to use sudo for some of these steps. 
https://tecadmin.net/setup-selenium-chromedriver-on-ubuntu/#comment-25215


Python imports
from selenium import webdriver #used to open the webpage
from bs4 import BeautifulSoup #used to parse HTML
import csv # used to write to csv
import datetime
import time
from pytz import timezone
import os #used to kill chrome sessions
import gc - used to clear memory
