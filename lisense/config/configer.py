# -*- coding: utf-8 -*-
"""
lisense.config.configer

This module helps in configuation management accross the project.
"""

from ConfigParser import RawConfigParser
from os.path import expanduser, join


class Configer:
    def __init__(self, init=False):
        self.config = RawConfigParser()
        self.section = 'Defaults'

        self.home_dir = expanduser('~')
        self.lisense_config = join(self.home_dir, '.lisense')

        if (init):
            self.initialize()

    def initialize(self):
        self.config.add_section(self.section)

    def dump(self, pairs):
        for pair in pairs:
            self.config.set(self.section, pair[0], pair[1])

        with open(self.lisense_config, 'wb') as f:
            self.config.write(f)

    def load(self, key):
        self.config.read(self.lisense_config)

        try:
            return self.config.get(self.section, key)
        except:
            return None
