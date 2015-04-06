# -*- coding: utf-8 -*-
"""
lisense.commands.listing

This module shows a listing of all the available licenses.
"""

from xtermcolor import colorize
from ..data.index import catalogue


def generate_list():
    """ Prints listing of all the available licenses.
    """

    print colorize("Lisense currently supports %d licenses.\n" %
                   (len(catalogue)),
                   ansi=4)

    for label, license in catalogue.iteritems():
        print colorize("- %s" % (license), ansi=253)


def check_license(license):
    """ Checks whether a given license is available or not.
    """

    if license in catalogue.keys():
        return True
    return False
