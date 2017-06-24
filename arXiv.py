docstr = """To download arXiv papers from terminal

Usage: 
    arXiv.py [options]

Options:
    -h, --help                  Print this message
    -d                          Download paper
    --get_info=<int>            Index of the paper that you want to get info or download
    --query=<str>               Query[Paper] that you want to search for 
    --max_result=<int>          Maximum Results to be retrieved [Default = 10]
    
"""






import requests
import urllib
import feedparser
from docopt import docopt
import os

base_url = "http://export.arxiv.org/api/query?"

search_query = "DeepLab"
start = 0
max_result = 10


feedparser._FeedParserMixin.namespaces['http://a9.com/-/spec/opensearch/1.1/'] = 'opensearch'
feedparser._FeedParserMixin.namespaces['http://arxiv.org/schemas/atom'] = 'arxiv'

''' A function to query from the arXiv API '''

def get_query():
    query = 'search_query=%s&start=%i&max_results=%i' % (search_query, start, max_result)
    response = urllib.urlopen(base_url+query).read() 
    feed = feedparser.parse(urllib.urlopen(base_url+query))
    if feed.get('status') != 200:
        raise Exception("HTTP Error " + str((feed.get('status', 'no status')) + " in query"))

    return feed

''' Function to print the list of papers that was queried for'''

def print_query(feed):
    for idx, entry in enumerate(feed.entries):
        print str(idx)+")", entry.title

''' Function to get information of a specific paper'''

def get_info(index, feed):
    entry = feed.entries[index]
    print "Title :", entry.title
    print "Published: ", entry.published.split('T')[0]
    print "Authors:  %s" % ', '.join(author.name for author in entry.authors)
    try:
        journal_ref = entry.arxiv_journal_ref
    except AttributeError:
        journal_ref = 'No Journal Reference found!'
    print 'Journal : %s' % journal_ref
    print "Summary :\n"
    print entry.summary, "\n"

def download_paper(get_info, feed):
    for link in feed.entries[get_info].links:
        if link.rel == 'alternate':
            abs_link =  link.href
        elif link.title == 'pdf':
            pdf_link =  link.href
    os.system("wget -U firefox "+ pdf_link + ".pdf")


if __name__ == "__main__":
    

    index = 1
    
    args = docopt(docstr, version='v0.1')
    print args
    
    if args["--max_result"]:
        max_result = int(args['--max_result'])
    
    search_query = args["--query"]
    if search_query:
        if args["--get_info"]:
            index = int(args['--get_info'])
            feed = get_query()
            get_info(index, feed)        
            if args["-d"]:
                download_paper(index, feed)
        else:
            feed = get_query()
            print_query(feed)    







