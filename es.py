
'''
>>> from elasticsearch import Elasticsearch
>>> ES_HOST = {"host": "localhost", "port": 9200}
>>> es = Elasticsearch(hosts=[ES_HOST])


We create an instance of Elasticsearch called es and assign it to port 9200 which is the default port for Elasticsearch.
Using the Elasticsearch instance we create an index called novels.

>>> INDEX_NAME = 'novels' 
>>> response = es.indices.create(index=INDEX_NAME)
>>> print(response)
{u'acknowledged': True, u'shards_acknowledged': True}

'''







import re
import time
import requests
from bs4 import BeautifulSoup
from elasticsearch import Elasticsearch

es_client = Elasticsearch(['http://localhost:9200'])
create_index = es_client.indices.create(index='blog-sysadmins', ignore=[400, 404])

drop_index = es_client.indices.delete(index='blog-sysadmins', ignore=400)
#create_index = es_client.indices.create(index='blog-sysadmins', ignore=[400, 404])

def urlparser(title, url):
    # scrape title
    p = {}
    post = title
    page = requests.get(post).content
    soup = BeautifulSoup(page, 'lxml')
    title_name = soup.title.string

    # scrape tags
    tag_names = []
    desc = soup.findAll(attrs={"property":"article:tag"})
    for x in xrange(len(desc)):
        tag_names.append(desc[x-1]['content'])

    # payload for elasticsearch
    doc = {
        'date': time.strftime("%Y-%m-%d"),
        'title': title_name,
        'tags': tag_names,
        'url': url
    }

    # ingest payload into elasticsearch
    res = es_client.index(index="blog-sysadmins", doc_type="docs", body=doc)
    time.sleep(0.5)

sitemap_feed = 'https://sysadmins.co.za/sitemap-posts.xml'
page = requests.get(sitemap_feed)
sitemap_index = BeautifulSoup(page.content, 'html.parser')
urls = [element.text for element in sitemap_index.findAll('loc')]

for x in urls:
    urlparser(x, x)




#curl -XGET 'localhost:9200/blog-sysadmins/_search?pretty=true&q=*:*'