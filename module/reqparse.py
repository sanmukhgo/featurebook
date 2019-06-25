""" Fetches and Parses the Inventory Features page into soup. """

import requests
from bs4 import BeautifulSoup as bs
import lxml
import html5lib


def parse(url, parser='html.parser', payload={}):
    """
    Returns parsed webpage as a BeautifulSoup object, 
    using the given parsers:

        lxml
        html5lib
        html.parser
    """

    r = requests.post(url, data=payload)
    
    if r.cookies:
        html = r.text
        return bs(html, parser)
    else:
        print(r.cookies)
        print("Login Unsuccessful")
        return None


_payload = {'os_username': 'sanmukh.s', 
            'os_password': 'Grey@1234'}
_url = 'https://work.greyorange.com/confluence/display/BS/40.+Inventory+Features'

soup = parse(_url, 'html5lib', _payload)

"""Tells if login was successful or not if invoked directly."""
if __name__ == "__main__":
    if soup:
        print("Login Successful")
