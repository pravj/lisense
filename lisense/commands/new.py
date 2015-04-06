# -*- coding: utf-8 -*-

"""
lisense.commands.new

This module generates a new License file in a directory according to
supplied arguments. 
"""

from os.path import abspath, dirname, expanduser, join
from xtermcolor import colorize
from .list import check_license
from ..data.index import catalogue
import ConfigParser
from jinja2 import Template


def create_license(license):
  if license is not None:
    if not check_license(license.lower()):
      print colorize("No such license named %s." % (license), ansi=196)
      print colorize("Use command 'lisense list' to see all available licenses.", ansi=196)
    else:
      print colorize("Generating %s license.." % (catalogue[license.lower()]), ansi=46)
      create_file(license.lower())
  else:
    home_dir = expanduser('~')
    lisense_config = join(home_dir, '.lisense')

    config = ConfigParser.RawConfigParser()
    config.read(lisense_config)

    default_license = config.get('Defaults', 'license')
    default_owner = config.get('Defaults', 'owner')

    print colorize("Generating default %s license.." % (default_license), ansi=46)
    generate_license(default_license.lower())


def generate_license(license):
  template_file_path = join(dirname(__file__), "../data/template/%s" % (license))
  template_file = abspath(template_file_path)

  with open(template_file) as f:
    content = f.read()

  template = Template(content)
  print template.render(owner="Pravendra Singh")
