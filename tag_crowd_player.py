# -*- coding: utf-8 -*-
import sys
import os
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.Firefox()
driver.implicitly_wait(3)

def open_TagCrowd():
    driver.get("http://tagcrowd.com/")
    driver.find_element_by_xpath("//input[@name='showFreq'][@type='radio'][@value='yes']").click()
    driver.find_element_by_link_text("Upload File").click()
    driver.implicitly_wait(3) 

def new_tab():
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')

def close_tab():
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w') 

def upload_abstract(file):
	driver.find_element_by_name("uploaded_file").send_keys(file)

def visualize():
    driver.find_element_by_link_text("Visualize!").click()

def file_list(path):
    listing = []
    for dirpath,dirnames, files in os.walk(path):
        for f in files:
            if f.lower().endswith(".txt"):
                fullpath = os.path.join(dirpath,f)
                listing.append(fullpath)
    return listing

def crawl(source):
    soup = BeautifulSoup(source, "lxml")
    content = soup.find_all(href = '#tagcloud')
    print content
    keywords = [ ]
    counts = [ ]
    for a in content:
        a_text = str(a)
        word_buffer = re.findall(r'>\w+<', a_text)
        keyword = re.findall(r'\w+', str(word_buffer))
        keywords.append(str(keyword))
        count = re.findall(r'[0-9]+', a_text)
        counts.append(str(count))
    return (keywords, counts)

def outcome_file(keywords, counts, locate, count):
    name = "keywords" + str(count) + ".txt"
    if os.path.exists(locate + name):
        print "File exists"
    else:
        os.chdir(locate)
        thefile = open(name, 'w')

    for n in range(0, len(keywords)):
        keyword = keywords[n]
        count = counts[n]
        thefile.write(keyword + "  " + count + "\n")
    thefile.close()

def TagCrowdAuto(path):
    files = file_list(path)
    count = 1
    for f in files:
        new_tab()
        open_TagCrowd()
        upload_abstract(f)
        visualize()
        source = driver.page_source
        keywords, counts = crawl(source)
        outcome_file(keywords, counts, path, count)
        close_tab()
        count += 1

TagCrowdAuto("/Users/Robert/Dropbox/abstracts")





