import requests
import urllib
import feedparser
import argparse





''' A function to query from the arXiv API '''
def query():
    url = 'http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1'
    data = urllib.urlopen(url).read()
    print data
    

query()








