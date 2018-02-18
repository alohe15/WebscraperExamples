#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 22:06:38 2017

@author: arnavlohe
"""

def word_frequency(url):
    import requests
    from bs4 import BeautifulSoup
    import re
    import pandas as pd

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    content = soup.find_all('p')
    st = ''
    for i in content:
        st = st + i.text
        st = st.lower()
    list_text = re.findall(r"[\w']+", st)
    list_set = list(set(list_text))
    word_freq = pd.Series(0, index = list_set)
    for word in list_text:
        if word in word_freq.index:
            word_freq[word] += 1
    return word_freq

def url_domain(url):
    a = url.split('.')
    domain = a[1]
    return domain

def file_frequency(url):
    domain = url_domain(url) + '.txt'
    file_object = open(domain, 'w+')
    series = word_frequency(url)
    for word in series.index:
        file_object.write(str(word))
        file_object.write(' ')
        file_object.write(str(series[word]))
        file_object.write('\n')
