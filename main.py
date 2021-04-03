import json
import copy
import pandas as pd
import numpy as np
from crawler import *
from text_processor import *

if __name__ == '__main__':
    # crawl data
    # # url link: Elsevier > Journals > Social Sciences > Geography, Planning and Development
    # url_catalogue = 'https://www.elsevier.com/catalog?producttype=journals&cat0=27390&cat1=28064&cat2=&q=&search=1&imprintname=&categoryrestriction=&sort=datedesc'

    # # get journal lists
    # crawler = page_crawler(url_catalogue)
    # parser = info_parser(crawler.get_soup())

    # #TODO use configuration file
    # tag = 'h5'
    # tag_class = 'listing-products-info-text-title'
    # journal_links = parser.crawl_link(tag, tag_class)
    # journal_titles = parser.crawl_title(tag, tag_class)
    # # print(journal_links)

    # whole_titles = {}
    # # get infos from journals
    # for i in tqdm(range(len(journal_links))):
    #     url_journal = journal_links[i] + "/recent-articles"
    #     journal_crawler = page_crawler(url_journal)
    #     journal_parser = info_parser(journal_crawler.get_soup())

    #     tag = 'div'
    #     tag_class = 'pod-listing-header'
    #     article_titles = journal_parser.crawl_title(tag, tag_class)
    #     whole_titles[journal_titles[i]] = article_titles
    
    # # keywords were not crawled to comply with robots.txt
    # # article_links = journal_parser.crawl_link(tag, tag_class)
    # # print(article_titles)
    # # print(article_links)

    # with open("0402_article_lists.json", 'w') as json_file:
    #     json.dump(whole_titles, json_file)

    
    # file path of the json file
    file_path = '0402_article_lists.json'

    # read the input
    with open(file_path, 'r') as f:
        article_lists = json.load(f)
    # print(json.dumps(article_lists, indent="\t"))

    processor = text_processor()
    print("Clean and combine all the texts")
    all_texts = ""
    for a in article_lists:
        for t in article_lists[a]:
            all_texts = all_texts + " " + t
    # print(all_texts)
    
    cleaned_texts = processor.clean_text(all_texts)
    frequency = processor.word_list_to_frequency(cleaned_texts)

    print("Check the most popular words")
    df = pd.DataFrame(list(frequency.items()), columns = ['vocabs', 'frequency'])
    df.sort_values('frequency', ascending=False)
    df_most_freq = df.nlargest(30, 'frequency')
    print(df_most_freq)


    # backup = copy.deepcopy(frequency)
    # for w in backup:
    #     if backup[w] == 1:
    #         del(frequency[w])
    #         continue
    # print(frequency)