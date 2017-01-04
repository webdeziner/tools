# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
from collections import defaultdict

occurrences = defaultdict(int)

__author__ = 'Webdeziner.se'

searchUrl = raw_input('Which url to scan: ');

def make_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, 'lxml')

def search(url):
    soup = make_soup(url)
    tags = soup.find_all()
    for tag in tags:
        occurrences[tag.name] += 1


    print len(tags)


search(searchUrl)

### print occurrences
for tag_count in occurrences:
    print tag_count, occurrences[tag_count]
