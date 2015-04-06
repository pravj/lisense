# -*- coding: utf-8 -*-
"""
lisense.commands.guide

This module shows common attributes about a particular license.
"""

from os.path import abspath, dirname, join
from .list import check_license
from xtermcolor import colorize
from yaml import load


def generate_guide(license):
    """ Checks availability of a particular license and proceed
    ahead accordingly. Alerts user about absense of the license.
    """

    if check_license(license.lower()):
        metadata_path = join(dirname(__file__), "../data/metadata/%s" %
                             (license.lower()))
        metadata_file = abspath(metadata_path)

        with open(metadata_file) as f:
            metadata = f.read()

        show_guide(load(metadata))
    else:
        print colorize("No such license named %s." % (license), ansi=4)
        print colorize(
            "Use command 'lisense list' to see all available licenses.")


def show_guide(metadata):
    """ Iterate through all the sections in metadata file of the license.
    Show colored attributes about any particular license
    """

    print colorize("%s" % (metadata['title']), ansi=4)
    print colorize("=" * len(metadata['title']), ansi=4)

    print colorize("\n[Description]", ansi=2)
    print colorize(metadata['description'], ansi=253)

    if 'note' in metadata.keys():
        print colorize("\n[Note]", ansi=3)
        print colorize(metadata['note'], ansi=253)

    if 'required' in metadata.keys():
        print colorize("\n[Required]", ansi=21)
        for attr in metadata['required']:
            print colorize("- %s" % (attr), ansi=253)

    if 'permitted' in metadata.keys():
        print colorize("\n[Permitted]", ansi=46)
        for attr in metadata['permitted']:
            print colorize("- %s" % (attr), ansi=253)

    if 'forbidden' in metadata.keys():
        print colorize("\n[Forbidden]", ansi=196)
        for attr in metadata['forbidden']:
            print colorize("- %s" % (attr), ansi=253)
