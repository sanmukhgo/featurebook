"""Merges all configuration tables of Inventory Features in one."""

from . import hdata


def get_configtable():
    """
    Returns combined configurations table as a dict of columns:

        .Source
        .Configuration
        .Description
        .Values
        .Default
    """

    configtable = {"Source": [], "Configuration": [],
                   "Description": [], "Values": [], "Default": []}
    data = hdata.data()                 # All data of the page

    for d in data:
        for tbl in d['table']:
            """Finds the table with particular headers"""

            if tbl[0] == ["Source", "Configuration", "Description", "Values", "Default"]:

                for row in tbl[1:]:  # Adding data to configtable
                    for (rdata, ctdata) in zip(row, configtable.values()):
                        ctdata.append(rdata)

    return configtable


if __name__ == "__main__":
    print(get_configtable())
