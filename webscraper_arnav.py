#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 22:06:38 2017

@author: arnavlohe
"""
url = 'https://www.bloomberg.com/quote/SPX:IND'

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
    print(word_freq)
    return word_freq
