# get_panels_from_panelapp
A script to download all panels from Panelapp.

Just launch it and it will download all panels listed in this webpage: [PanelApp](https://panelapp.genomicsengland.co.uk/panels/). The spaces present in the names of the downloaded tsv files are replaced by _

The script downloads all the tsv files in the directory where you launch it:

```
./get_panels_from_panelapp.py

https://panelapp.genomicsengland.co.uk/panels/1141/download/01234/
100% [..............................................................................] 23867 / 23867https://panelapp.genomicsengland.co.uk/panels/399/download/01234/
100% [................................................................................] 4971 / 4971https://panelapp.genomicsengland.co.uk/panels/933/download/01234/
100% [................................................................................] 5019 / 5019https://panelapp.genomicsengland.co.uk/panels/929/download/01234/
100% [................................................................................] 2566 / 2566https://panelapp.genomicsengland.co.uk/panels/930/download/01234/
100% [................................................................................] 3099 / 3099https://panelapp.genomicsengland.co.uk/panels/934/download/01234/
100% [................................................................................] 3888 / 3888https://panelapp.genomicsengland.co.uk/panels/931/download/01234/
100% [................................................................................] 2644 / 2644https://panelapp.genomicsengland.co.uk/panels/932/download/01234/
100% [................................................................................] 1884 / 1884https://panelapp.genomicsengland.co.uk/panels/774/download/01234/
100% [..................................................................................] 866 / 866https://panelapp.genomicsengland.co.uk/panels/540/download/01234/
...
```

## Dependencies

The scripts depends on two python packaces:

* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).
* [wget](https://pypi.org/project/wget/).

## Installation of dependencies:

```
pip install bs4 wget
```
