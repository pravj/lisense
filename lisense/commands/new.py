# -*- coding: utf-8 -*-

"""
lisense.commands.new

This module generates a new License file in a directory according to
supplied arguments. 
"""

from os.path import abspath, dirname, join
from xtermcolor import colorize
from datetime import datetime
from .list import check_license
from ..data.index import catalogue
from ..config.configer import Configer
from jinja2 import Environment, Template, meta


def parse_template(template):
  env = Environment()
  ast = env.parse(template)
  return meta.find_undeclared_variables(ast)


def create_license(license, owner):
  configer = Configer()

  if license is not None:
    if not check_license(license.lower()):
      print colorize("No such license named %s." % (license), ansi=196)
      print colorize("Use command 'lisense list' to see all available licenses.", ansi=196)
    else:
      print colorize("Generating %s license.." % (catalogue[license.lower()]), ansi=46)
      generate_license(license.lower(), owner)
  else:
    if configer.load('license') is not None:
      default_license = configer.load('license')
      print colorize("Generating default %s license.." % (default_license), ansi=46)
      generate_license(default_license.lower(), owner)
    else:
      print colorize("No license associated in the configuration.", ansi=196)
      print colorize("Use command 'lisense setup' to setup default global configuration.", ansi=196)


def generate_license(license, owner):
  configer = Configer()

  if owner is None:
    if configer.load('owner') is None:
      print colorize("No owner associated in the configuration.", ansi=196)
      print colorize("Use command 'lisense setup' to setup default global configuration.", ansi=196)
    else:
      print colorize("Using \"%s\" as the owner for license.." % (configer.load('owner')), ansi=46)  
      owner = configer.load('owner')
  else:
    print colorize("Using \"%s\" as the owner for license.." % (owner), ansi=46)

  generate_license_file(license, owner)


def generate_license_file(license, owner):
  template_file_path = join(dirname(__file__), "../data/template/%s" % (license))
  template_file = abspath(template_file_path)

  with open(template_file) as f:
    content = f.read()

  parsed_context = parse_template(content)
  default_context_keys = ['owner', 'year']

  context = {'year': datetime.now().year, 'owner': owner}
  extra_context = {}

  if (len(parsed_context) > len(default_context_keys)):
    for key in parsed_context:
      if key not in default_context_keys:
        print colorize("\n%s license also asks for %s. What do you want to fill there?" % (license, key), ansi=4)
        extra_context[key] = raw_input().strip()

  arguments = context.copy()
  arguments.update(extra_context)

  template = Template(content)
  print template.render(arguments)
