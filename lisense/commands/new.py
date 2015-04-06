# -*- coding: utf-8 -*-

"""
lisense.commands.new

This module generates a new License file in a directory according to
supplied arguments. 
"""

from os.path import expanduser, join
from xtermcolor import colorize
from .list import check_license
import ConfigParser


def generate_license(license):
  if license is not None:
    if not check_license(license.lower()):
      print colorize("No such license named %s." % (license), ansi=196)
      print colorize("Use command 'lisense list' to see all available licenses.", ansi=196)
    else:
      print colorize("Generating %s license.." % (license), ansi=46)
  else:
    home_dir = expanduser('~')
    lisense_config = join(home_dir, '.lisense')

    config = ConfigParser.RawConfigParser()
    config.read(lisense_config)

    default_license = config.get('Defaults', 'license')
    default_owner = config.get('Defaults', 'owner')

    print colorize("Generating default %s license.." % (default_license), ansi=46)
