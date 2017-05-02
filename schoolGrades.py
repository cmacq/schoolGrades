# -*- coding: utf-8 -*-
"""
Created on Tue May  2 01:01:37 2017

@author: user1
"""

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent



ua = UserAgent()
header = {'user-agent':ua.chrome}
google_page = requests.get('https://calendar.google.com/calendar/htmlembed?src=lexington.k12.il.us_trqdg10lkf759nbhfijho33i2g@group.calendar.google.com&amp;amp;color=%23668CD9&amp;amp;mode=AGENDA&amp;amp;showTitle=1&amp;amp;showNav=1&amp;amp;showDate=1&amp;amp;showTabs=1&amp;amp;showCalendars=0&amp;amp;hl=en&mode=AGENDA&dates=20170101/20170201',headers=header)
soup = BeautifulSoup(google_page.content,'lxml') # html.parser
print(soup.prettify)
link = soup.a
    