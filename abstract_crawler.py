from bs4 import BeautifulSoup
import requests
import re
import sys
import os.path

# Readme:
# 1. follow the guide to input the start year and end year you want to crawl
# 2. wait for the abstract spiders to collect content, if there is anything wrong it will generate an error message
# 3. when the crawling is finished, it will save the outcome as a text file, name it and set a location to store it

def archive_spider(year_to_start, year_to_end):
    year = year_to_start
    archive_list = []
    while year_to_start <= year <= year_to_end:
        url = "http://arxiv.org/year/cond-mat/" + str(year)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")
        for links in soup.findAll('a', href = re.compile(r"/list/cond-mat/"), text = re.compile(r"[0-9]{4}$")):
            archive_list.append("http://arxiv.org/list/cond-mat/" + links['href'][-4:])
        year += 1
    return archive_list

def title_spider(link):
    url = link
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")
    title_list = []
    for links in soup.findAll('a', href = True, title = re.compile(r'Abstract')):
        title_list.append("http://arxiv.org/" + links['href'])
    return title_list

def abstract_spider(link):
    url = link
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")
    abstract_block = str(soup.findAll(class_ = "abstract mathjax"))
    abstract_start = int(abstract_block.index('</span>') + 8)
    abstract = abstract_block[abstract_start: -16]
    return abstract


def get_abstract(year_start, year_end):
    print "Please wait for our little spiders to collect abstracts, it will take around one minute for one year's content."
    archive = archive_spider(year_start, year_end)
    abstract = ""
    for links in archive:
        title_list = title_spider(links)
        for titles in title_list:
            abstract += abstract_spider(titles)
            # print abstract
    save_to_txt(abstract)

def save_to_txt(abstract):
    print 'creating new text file'
    name_of_file = raw_input('Input name of the text file:') + '.txt'
    save_path = raw_input('Where you want to save it:')
    complete_name = os.path.join(save_path, name_of_file)

    try:
        file = open(complete_name, 'w')
        file.write(abstract + "\n")
        file.close()
    except:
        print 'There is something wrong!'
        sys.exit(0)

def run_crawler():
    year_start = input("Which year you want to start? Type in the last two digit of the year. (e.g. 2015 --- 15)")
    year_end = input("Which year you want to end? Type in the last two digit of the year. (e.g. 2015 --- 15)")
    get_abstract(year_start, year_end)

run_crawler()
