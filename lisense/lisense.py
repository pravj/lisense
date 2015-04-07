"""Lisense - Sensible repository licensing for Humans

Usage:
  lisense list
  lisense setup
  lisense new [<license>] [--owner=name]
  lisense guide <license>
  lisense -h | --help
  lisense --version

Options:
  -h --help       Show help message.
  --version       Show version.
  --owner=name    Owner for the license.
"""


from docopt import docopt
from parser.parser import ArgumentParser


def main():
    arguments = docopt(__doc__, version="1.1.0")
    parser = ArgumentParser(arguments)
    parser.action()

if __name__ == "__main__":
    main()
