# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 14:57:28 2019

@author: Zac_Fang
"""

# Define report_status
def report_status(**kwargs):
    """Print out the status of a movie character."""
    print(type(kwargs))
    print(kwargs)
    print("\nBEGIN: REPORT\n")

    # Iterate over the key-value pairs of kwargs
    for key, value in kwargs.items():
        # Print out the keys and values, separated by a colon ':'
        print(key + ": " + value)
    print("\nEND REPORT")
# First call to report_status()
report_status(name="luke", affiliation="jedi", status="missing")
# Second call to report_status()
report_status(name="anakin", affiliation="sith lord", status="deceased")

def report_args(*args):
    """Print out the status of a movie character."""
    print(type(args)) # return tuple type
    print(args)
# First call to report_status()
report_args("luke","jedi","missing")
# Second call to report_status()
report_args("anakin","sith lord","deceased")