#!/usr/bin/env python

import sys
import os
import fnmatch
from bs4 import BeautifulSoup

# Open a text file.
txtfile = open('dhq.txt', 'w')

# Loop over directories.
for (indexnumber, (dirpath, dirs, files)) in enumerate(os.walk('.')):

    # Loop over files with .xml extension.
    for (num, filename) in enumerate(fnmatch.filter(files, '*.xml')):

        # Build file path.
        filepath = os.path.join(dirpath, filename)

        # Open XML file, strip its tags, and write contents to our text file.
        with open(filepath) as f:
            soup = BeautifulSoup(f.read())
            paragraphs = soup.select('body p')

            for (paranum, paragraph) in enumerate(paragraphs):
                text = paragraph.getText()
                text = ' '.join(text.split())
                text = text.encode('utf-8')
                column = str(paranum) + filename
                txtfile.write(column + "\t" + column + "\t" + text)
                txtfile.write('\n')
