""" Parses the Inventory Features page as "soup". """

from bs4 import BeautifulSoup as bs
from . import reqpage
import lxml
import html5lib


def _parse(location: str, parser: str):
    """
    Returns parsed page at "location as a BeautifulSoup object, 
    using the given parsers:

        lxml
        html5lib
        html.parser
    """
    try:
        f = open(location, "r")
    except:
        reqpage.save_inventory()
        return _parse(location,parser)

    return bs(f.read(), parser)
    f.close()


_html = "page/inventory.html"
_parser = "lxml"

soup = _parse(_html, _parser)

"""Prints the page, if invoked directly."""
if __name__ == "__main__":
    print(soup.prettify)
