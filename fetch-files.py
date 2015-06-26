#!/usr/bin/env python

import urllib2
import os
from bs4 import BeautifulSoup

soup = BeautifulSoup(urllib2.urlopen("http://www.digitalhumanities.org/dhq/index/author.html"))

articles = soup.select("p.index_top a")

dhqbase = "http://www.digitalhumanities.org"

for article in articles:
    url = article.get('href')

    articledir = os.path.dirname(url)

    # Build the XMLURL to fetch
    xmlurl = dhqbase + articledir + ".xml"

     # dhq-vol-7-2-000121.xml
    filename = articledir.replace("/", "-") + ".xml"

    try:
     # Fetch teh XML file
        response = urllib2.urlopen(xmlurl)

        # Open a new file locally, save contents of XML to it.
        with open(filename, 'w') as f:
            f.write(response.read())
        response.close()

    except urllib2.URLError as e:
        print xmlurl
