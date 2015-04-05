# -*- coding: utf-8 -*-

"""
lisense.parser.parser

This module parses command-line arguments and act accordingly.
"""

from ..data.index import catalogue
from ..commands.list import generate_list

class ArgumentParser:

  def __init__(self, args):
    self.args = args

  def action(self):
    if self.args['list']:
      generate_list()
    elif self.args['new']:
      print self.args['<license>']
      print "create new license"
    elif self.args['setup']:
      print "setup configuration"
    elif self.args['guide']:
      print "guide about %s license" % (self.args['<license>'])
