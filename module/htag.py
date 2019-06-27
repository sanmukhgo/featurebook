"""Collects all h-tags of Inventory Features page."""

from .parsepage import soup


def _get_htags():
    """Returns list of all h-tags (unformatted). """

    """
    div: The div-tag containing all content.
    hlist: List of particular h-tags searched for in div.
    headings: List of found headings.
    """

    div = soup.find('div', {'id': 'main'})
    hlist = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    htags = div.find_all(hlist)

    return htags


def headings():
    """
    Returns a list of dict of all headings with their tag.

        .tag: Tag name
        .text: Text inside tag 
    """

    htags=_get_htags()

    headings = []
    for h in htags:
        tag = h.name
        text = h.text.strip()
        headings.append({"tag": tag, "text": text})

    return headings


def print_headings():
    """Prints all headings with proper indentation and line spacing."""
    """
    Gives Indentation based on hn1.
    Gives Newline based on comparing hn1 and hn2.

    hn1: Index of current h-tag
    hn2: Index of next h-tag
    headings: Stores all h-tags data
    spc: 1 tab space 
    """

    htags=_get_htags()

    hlen = len(htags)
    spc = "   "
    for i in range(hlen):
        hn1 = int(htags[i].name[1])
        if i < hlen-1:         # boundary check
            hn2 = int(htags[i+1].name[1])

        indent = spc*(hn1-1)
        print(indent, end="")  # puts indentation
        txt = (htags[i].text.strip())
        print(txt)             # puts heading
        if hn1 > hn2:
            print()            # puts newline


""" Prints all headings if invoked directly."""
if __name__ == "__main__":
    print_headings()
