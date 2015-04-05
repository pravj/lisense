"""
lisense.commands.listing

This module shows a listing of all the available licenses.
"""

from ..data.index import catalogue


def generate_list():
  for k, v in catalogue.iteritems():
    print k
