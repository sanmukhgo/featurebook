"""Collects all h-tags of Inventory Features page."""

from .parsepage import soup


def headings():
    """
    Returns a list of dict of all headings with their tag.

        .tag: Tag name
        .text: Text inside tag 
    """

    headings = []
    for h in _htags:
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

    hlen = len(_htags)
    spc = "   "
    for i in range(hlen):
        hn1 = int(_htags[i].name[1])
        if i < hlen-1:         # boundary check
            hn2 = int(_htags[i+1].name[1])

        indent = spc*(hn1-1)
        print(indent, end="")  # puts indentation
        txt = (_htags[i].text.strip())
        print(txt)             # puts heading
        if hn1 > hn2:
            print()            # puts newline


"""
div: The div-tag containing all content.
hlist: List of particular h-tags searched for in div.
headings: List of found headings.
"""
_div = soup.find('div', {'id': 'main'})
_hlist = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
_htags = _div.find_all(_hlist)

""" Prints all headings if invoked directly."""
if __name__ == "__main__":
    h=headings()
    print(h)
    #print_headings()
