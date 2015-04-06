# -*- coding: utf-8 -*-
"""
lisense.commands.setup

This module deals with the initial global configuration setup for the lisense
"""

from xtermcolor import colorize
from os.path import expanduser, join
from sys import exit
from .list import check_license, generate_list
from ..data.index import catalogue
from ..config.configer import Configer


def setup_lisense():
    """ Configure global lisense settings by asking user about the defaults.
    """

    print colorize(
        "This utility will configure Lisense globally on your system.",
        ansi=4)
    print colorize(
        "Lisense will use this configuration to generate licenses, in case you don't provide any arguments.\n",
        ansi=4)

    print colorize(
        "1. Enter default license that you want to use in your projects?",
        ansi=253)
    default_license = raw_input().strip()

    if check_license(default_license.lower()):
        pass
    else:
        print colorize(
            "No such license named %s.\nUse command 'lisense list' to see all available licenses."
            % (default_license),
            ansi=196)
        exit()

    print colorize(
        "\n2. Enter default owner name that you want to use in your projects?",
        ansi=253)
    default_owner = raw_input().strip()

    set_config(default_license, default_owner)


def set_config(license, owner):
    """ Set default template context variables in the global configuration.
    """

    configer = Configer(True)
    configer.dump([['license', catalogue[license.lower()]], ['owner', owner]])
