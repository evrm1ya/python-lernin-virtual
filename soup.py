# Problem 14
# Use BeautifulSoup to extract all HTML links from a webpage

import sys
import urllib
from bs4 import BeautifulSoup
import json

def main(url, writepath):
    response = urllib.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    handle = open(writepath, 'w')
    handle.write(json.dumps(links, indent=2))
    handle.close

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

