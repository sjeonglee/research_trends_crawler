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
    frequency_1_gram = processor.word_list_to_frequency(cleaned_texts)
    print("Check the most popular 1-gram-words")
    df_1 = pd.DataFrame(list(frequency_1_gram.items()), columns = ['vocabs', 'frequency'])
    df_1.sort_values('frequency', ascending=False)
    df_1.to_csv('one_gram_counted.csv')

    df_most_freq = df_1.nlargest(50, 'frequency')
    print(df_most_freq)

    # 2 gram vocabularies
    processor.set_gram(2)
    cleaned_texts = processor.clean_text(all_texts)
    frequency_2_gram = processor.word_list_to_frequency(cleaned_texts)
    print("Check the most popular 2-gram-words")
    df_2 = pd.DataFrame(list(frequency_2_gram.items()), columns = ['vocabs', 'frequency'])
    df_2.sort_values('frequency', ascending=False)
    df_2.to_csv('two_gram_counted.csv')

    # df_most_freq = df_2.nlargest(30, 'frequency')
    # print(df_most_freq)

    # 3 gram vocabularies
    processor.set_gram(3)
    cleaned_texts = processor.clean_text(all_texts)
    frequency_3_gram = processor.word_list_to_frequency(cleaned_texts)
    print("Check the most popular 3-gram-words")
    df_3 = pd.DataFrame(list(frequency_3_gram.items()), columns = ['vocabs', 'frequency'])
    df_3.sort_values('frequency', ascending=False)
    df_3.to_csv('three_gram_counted.csv')

    # df_most_freq = df_3.nlargest(30, 'frequency')
    # print(df_most_freq)

    # backup = copy.deepcopy(frequency)
    # for w in backup:
    #     if backup[w] == 1:
    #         del(frequency[w])
    #         continue
    # print(frequency)