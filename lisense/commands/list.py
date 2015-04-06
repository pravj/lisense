# -*- coding: utf-8 -*-

"""
lisense.commands.listing

This module shows a listing of all the available licenses.
"""

from xtermcolor import colorize
from ..data.index import catalogue


def generate_list():
  print colorize("Lisense currently supports %d licenses\n" % (len(catalogue)), ansi=4)

  index = 1
  for label, license in catalogue.iteritems():
    print "%d. %s" % (index, license)
    index += 1


def check_license(license):
  if license in catalogue.keys():
    return True
  return False
