""" Collects all hyperlinks to external pages in Inventory Features page."""

from .parsepage import soup


def links(key=''):
    """
    Returns a list of dict of all links starting with 'key'.

        .url: Page URL
        .text: URL text 
    """

    links = []
    for i in a_list:
        if i['href'].startswith(key):
            url = i['href']
            text = i.text.strip()
            links.append({"url": url, "text": text})
    return links


def print_links(key='http'):
    """Prints all link data which starts with key."""

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
