import sys
sys.path.insert(0, '..')

import pandas as pd 

urls = pd.read_csv('./test_files/blog_urls.csv')

from seoworkflows_lib.scrapers.beautiful_soup.xpath_single_page import xpath_single_page
from seoworkflows_lib.nlp.tf_idf import tfidf

# xpath='//div[@class="entry-content"]'
xpath='//head//title'
crawl_data = xpath_single_page(urls=urls.head(30), xpath=xpath, text_only=True)
# print(crawl_data.head(3))

tfidf_data = tfidf(df = crawl_data)
print(tfidf_data)

