#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import datetime
from bs4 import BeautifulSoup
import random
from time import sleep
import pynotify
news=""

while True:
    try:

        sc = requests.get('http://www.ratopati.com/')
        soup = BeautifulSoup(sc.text,'lxml')
        for div in soup.findAll('div',{'class':'photoFeature'}):
            new=div.find('ul')
            for li in new.findAll('li'):
                # print li.h1.text
                news+=" ** "+li.h1.text+'\n'
            print news

                       # basic = soup.select('h5 > a')
        # news = head + basic
        while True:

            pynotify.init('test')
            n = pynotify.Notification('Live News from Ratopati',"*" +news)
            n.show()
            break
    except requests.exceptions.ConnectionError:
        pynotify.init('test')
        n = pynotify.Notification('Connection Issue','No internet found')
        n.show()
    sleep(60)
