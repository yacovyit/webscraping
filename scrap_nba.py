#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 22:22:54 2017

@author: yacovyitzhak
"""

from selenium import webdriver
from bs4 import BeautifulSoup
#create driver
driver = webdriver.PhantomJS(executable_path ="/Users/yacovyitzhak/Documents/chrome/phantomjs-2.1.1-macosx/bin/phantomjs")

url = "http://stats.nba.com/players/list/"
driver.get(url)

print (driver.page_source)