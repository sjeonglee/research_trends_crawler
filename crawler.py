import json
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# web page crawler: crawl web page file from the given url
class page_crawler():
    def __init__(self, url):
        self.url = url
        self.response = self.get_response()
    
    # get response from the url
    def get_response(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            print("Successfully get response")
            return response
        else:
            print("Failed to get response", response.status_code)
            return None
    
    # get beautifulsoup from html page
    def get_soup(self):
        html = self.response.text
        return BeautifulSoup(html, 'html.parser')

# information parser
class info_parser():
    def __init__(self, soup:BeautifulSoup):
        self.soup = soup

    # get journal links (only valid for catalogue page)
    def crawl_link(self, tag:str, tag_class:str):
        links = []
        search_result = self.soup.find_all(tag, tag_class)
        for result in search_result:
            li = result.find('a').get('href')
            if li != None:
                links.append(li)
        return links

    # get journal links (only valid for catalogue page)
    def crawl_title(self, tag:str, tag_class:str):
        titles = []
        search_result = self.soup.find_all(tag, tag_class)
        for result in search_result:
            ti = result.find('a').get_text()
            if ti != None:
                titles.append(ti.strip())
        return titles
        # journal_tags = search_result.find_all('div')
        # print(journal_tags)
        # journal_titles = self.soup.select_one('#maincontent > section.listing-content.clearfix > div.listing-section-products.clearfix > div:nth-child(1) > div.listing-products-info > div > div.listing-products-info-text > h5 > a')
        # print(journal_titles.get_text())
        # return journal_titles.get_text()

    # get journal keywords (unable to proceed only to comply with robots.txt)
    def crawl_keyword(self, tag:str, tag_class:str):
        keywords = []
        search_result = self.soup.find_all(tag, tag_class)
        for result in search_result:
            key = result.find('span').get_text()
            if key != None:
                keywords.append(key)
        return keywords

    # to check if soup is not empty
    def print_soup(self):
        print(self.soup)