# arXiv_download
A python script that you can execute form terminal to directly download a paper that you want form arXiv

# Installation
To install follow the steps:

 1. `wget https://pypi.python.org/packages/87/03/0b6503d32ae1bb173c24f12430dd46ad46ee152fe149bcd0c62c9a7c17d6/arXiv_download-0.1.tar.gz`
 2. `tar -xvzf arXiv_download-0.1.tar.gz`
 3. cd arXiv_download-0.1`
 4. python setup.py install`
# Options

There are multiple options that you can use.
1) `--query` : To search for papers
2) `--get_info` : To get information such as the authors, summary, published date etc. of a single paper
3) `-d` : To download the paper.
4) `--max_results` : How many results to display

# Examples

 - `arXiv --query="DeepLab" --max_results=10` - displays 10 results for the query
 - `arXiv --query="DeepLab" --get_info=4`- Displays the summary of the 4th option
 - `arXiv --query="DeepLab" --get_info=4 -d` - Downloads the paper
