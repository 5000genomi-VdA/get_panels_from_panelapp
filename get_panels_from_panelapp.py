#!/usr/bin/env python

import argparse
import gzip
import argparse
from bs4 import BeautifulSoup
import urllib.request
import wget
import os

def get_panels(page_url):
        items = []
        fp = urllib.request.urlopen(page_url)
        soup = BeautifulSoup(fp, features="html.parser")
        trs = soup.find_all("tr")
        for tr in trs:
            if tr.get("data-panel"):
                for a in  tr.find_all("a"):
                    if a.get("href"):
                        url = a.get("href").startswith("/panels/") and "download" in a.get("href").split("/")
                        if url:
                            download_link = "https://panelapp.genomicsengland.co.uk" + a.get("href")
                            print(download_link)
                            filename = wget.download(download_link)
                            os.rename(filename,  filename.replace(" ", "_"))

def main():
    parser = argparse.ArgumentParser(description="Download all panels from panelapp")
    args = parser.parse_args()

    get_panels("https://panelapp.genomicsengland.co.uk/panels")

if __name__ == "__main__":
    main()
