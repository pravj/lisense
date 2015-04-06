import os
from setuptools import setup


# read content from utility files
def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
    name='lisense',
    version='0.0.1',
    author='Pravendra Singh',
    author_email='hackpravj@gmail.com',
    description=('Sensible repository licensing for Humans'),
    license = 'MIT',
    keywords = 'git github bitbucket repository license',
    url = 'https://github.com/pravj/lisense',
    packages=['lisense', 'lisense.parser', 'lisense.data', 'lisense.commands', 'lisense.config'],
    package_data = {
      'lisense': ['data/template/*', 'data/metadata/*']
    },
    install_requires=['docopt', 'jinja2', 'xtermcolor'],
    long_description=read('README.rst'),
    entry_points={
        'console_scripts': ['lisense = lisense.lisense:main']
    }
)
