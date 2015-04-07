import os
from setuptools import setup


# read content from utility files
def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
    name='lisense',
    version='1.1.0',
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
    install_requires=['docopt', 'jinja2', 'pyyaml', 'xtermcolor'],
    long_description=read('README.rst'),
    entry_points={
        'console_scripts': ['lisense = lisense.lisense:main']
    },
    classifiers = [
      'Development Status :: 5 - Production/Stable',
      'Environment :: Console',
      'Operating System :: OS Independent',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: MIT License',
      'Natural Language :: English',
      'Programming Language :: Python :: 2.6',
      'Programming Language :: Python :: 2.7',
      'Topic :: Software Development :: Version Control'
    ]
)
