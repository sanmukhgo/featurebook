"""
Collects all data of Inventory Features page, 
under their respective h-tags.
"""
from .parsepage import soup


def _parse_list(tag):
    """ Used for nested html lists."""

    if tag.name == 'ul':
        return [_parse_list(item)
                for item in tag.find_all('li', recursive=False)]

    elif tag.name == 'li':
        if tag.ul is None:
            return tag.text
        else:
            return [tag.contents[0].string.strip(), _parse_list(tag.ul)]


def data():
    """
    Returns a list of dict with all data.

        .tag: h-Tag name
        .text: Tag heading
        .ul: Data stored as unordered list
        .table: Data stored in tables
        .subheads: h-Tags under the current tag
    """

    data = []
    m = soup.find('div', {'id': 'main-content'})

    for tag in m.children:

        """Creates dict element with tag name and text for h-tags."""
        if tag.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            data.append({'tag': tag.name,
                         'text': tag.text.strip(),
                         'ul': [],
                         'table': [],
                         'subheads': []})

        """Adds unordered list data."""
        if tag.name == 'ul':
            temp = _parse_list(tag)
            data[-1]['ul'].append(temp)

        """Adds tabular data."""
        try:
            lst = tag.get_attribute_list('class') # Finds table
            if 'table-wrap' in lst:
                tbl = []
                row = []

                for j in tag.find_all('tr'):      # Adds table rows
                    row = []

                    for k in j.children:
                        if k.name == "th" or k.name=="td":
                            '''txt = _parse_list(l.ul)
                            if txt == None:'''
                            txt = k.get_text('\n ').strip()
                            row.append(txt)  

                    if row != []:
                        tbl.append(row)

                if(tbl != []):
                    data[-1]['table'].append(tbl)
        except:
            pass

    return data


def print_data():
    """Prints all Inventory Features data."""

    d = data()
    for i in d:
        for key, value in i.items():
            print(key, " : ", value)
        print()

""" Prints all data if invoked directly."""
if __name__ == "__main__":
    print_data()
