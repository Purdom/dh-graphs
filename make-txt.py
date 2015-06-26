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
            text = soup.getText()
            txtfile.write(text.encode("utf-8"))
            txtfile.write('\n')
