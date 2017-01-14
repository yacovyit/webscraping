#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 22:22:54 2017

@author: yacovyitzhak
"""

from selenium import webdriver
from bs4 import BeautifulSoup

class Player():
    def __init__(self):
        self.name = ""
        self.link = ""
    def toString(self):
        return self.name + ", " + self.link
        
def get_player_list():
    #create driver
    driver = webdriver.PhantomJS(executable_path ="/Users/yacovyitzhak/Documents/chrome/phantomjs-2.1.1-macosx/bin/phantomjs")
    
    url = "http://stats.nba.com/players/list"
    player_url = "http://stats.nba.com"
    #get content
    driver.get(url)
    
    
    #create soap
    soap = BeautifulSoup(driver.page_source,'lxml')
    
    #find elements
    div = soap.find('div', class_='stats-player-list players-list ng-scope')
    player_list = []
    for a in div.find_all('a'):
        player = Player()
        player.name = a.text
        player.link = player_url + a['href']
        player_list.append(player)
    
    
    #close driver
    driver.quit
    return player_list
    
players = get_player_list()
for player in players:
        print(player.toString())
            
