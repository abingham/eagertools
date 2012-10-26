import sys

import distribute_setup
distribute_setup.use_setuptools()

from setuptools import setup, find_packages

setup(
    name = 'eagertools',
    version = '0.1',
    packages = find_packages(),

    # metadata for upload to PyPI
    author = 'Austin Bingham',
    author_email = 'austin.bingham@gmail.com',
    description = 'Eager version of some lazy functions.',
    license = 'MIT',
    keywords = '',
    url = 'http://github.com/abingham/eagertools',
)
