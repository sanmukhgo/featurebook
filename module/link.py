""" Collects all hyperlinks to external pages in Inventory Features page."""

from .parsepage import soup

def get_a_list():
    """Returns list of all <a> tags."""

    a_list = soup.find_all('a', href=True)
    return a_list

def links(key='http'):
    """
    Returns a list of dict of all links.

        .url: Page URL
        .text: URL text 
    """

    a_list=get_a_list()

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


""" Prints all links containing key if invoked directly."""
if __name__ == "__main__":
    print("Enter key: ", end=" ")
    key = str(input())

    print_links(key)
