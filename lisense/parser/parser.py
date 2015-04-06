# -*- coding: utf-8 -*-

"""
lisense.parser.parser

This module parses command-line arguments and act accordingly.
"""

from ..data.index import catalogue
from ..commands.list import generate_list
from ..commands.new import create_license
from ..commands.setup import setup_lisense
from ..commands.guide import generate_guide

class ArgumentParser:

  def __init__(self, args):
    self.args = args

  def action(self):
    if self.args['list']:
      generate_list()
    elif self.args['new']:
      create_license(self.args['<license>'])
    elif self.args['setup']:
      setup_lisense()
    elif self.args['guide']:
      generate_guide(self.args['<license>'])
