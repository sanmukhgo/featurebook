""" Fetches the Inventory Features page. """

import requests


def _fetch_page(url: str, payload: dict = {}):
    """
    Returns fetched webpage as a request object
    """

    r = requests.post(url, data=payload)

    if r.cookies:
        return r
    else:
        print("Login Unsuccessful")
        return None


def save_inventory(name: str = "inventory"):
    """
    Saves the fetched webpage into "name".html file.
    """

    try:
        page = fetch_inventory().text
    except:
        return None

    f = open("page/"+name+".html", "w")
    f.write(page)
    f.close()


def fetch_inventory():
    """
    Returns Inventory Features webpage as a request object
    """

    payload = {'os_username': 'sanmukh.s',
               'os_password': 'Grey@1234'}
    url = 'https://work.greyorange.com/confluence/display/BS/40.+Inventory+Features'

    return _fetch_page(url, payload)



"""Tells if login was successful or not, if invoked directly."""
if __name__ == "__main__":
    if fetch_inventory():
        print("Login successful")
        save_inventory()
