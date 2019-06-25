""" Collects all hyperlinks to external pages in Inventory Features page."""

from .reqparse import soup


def links(key='http'):
    """ Returns all links which starts with key."""

    links = []
    for i in a_list:
        if i['href'].startswith(key):
            links.append(i['href'])
    return links


def print_links(key='http'):
    """Prints all links which starts with key."""

    lst = links(key)
    for i in lst:
        print(i)


""" 
a_list: List of all <a> tags.
links(): Returns list of direct http links.
print_links(): Prints all http links
"""
a_list = soup.find_all('a', href=True)

""" Prints all links containing key if invoked directly."""
if __name__ == "__main__":
    print("Enter key: ", end=" ")
    key = str(input())

    print_links(key)
