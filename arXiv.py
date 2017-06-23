import requests
import urllib
import feedparser
import argparse



base_url = "http://export.arxiv.org/api/query?"

search_query = "DeepLab"
start = 0
max_result = 5

query = 'search_query=%s&start=%i&max_results=%i' % (search_query, start, max_result)

feedparser._FeedParserMixin.namespaces['http://a9.com/-/spec/opensearch/1.1/'] = 'opensearch'
feedparser._FeedParserMixin.namespaces['http://arxiv.org/schemas/atom'] = 'arxiv'

''' A function to query from the arXiv API '''

def get_query():
    response = urllib.urlopen(base_url+query).read() 
    feed = feedparser.parse(urllib.urlopen(base_url+query))
    print feed.get('status')
    if feed.get('status') != 200:
        raise Exception("HTTP Error " + str((feed.get('status', 'no status')) + " in query"))

    return feed

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




if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Display Research Papers from arXiv.org and download from terminal itself!"
    )
    
    parser.add_argument("query", default="DeepLab", type=str, nargs='*',
                        help="Research Paper that you want to search")
    
    args = parser.parse_args()
    print args.query 


    feed = get_query()
    index = 1
    get_info(index, feed)







