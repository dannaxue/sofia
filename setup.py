#!/usr/bin/env python
"""Setup script for installing sofia."""

from setuptools import setup 

config = {
    'name': 'sofia',
    'version': '1',
    'description': 'GUI',
    'author': 'Danna Xue',
    'author email': 'dannaxue@stanford.edu',
    'url': 'https://github.com/dannaxue/sofia.git',
    'download_url': 'https://github.com/dannaxue/sofia',
    'license': 'MIT',
    'packages': ['sofia'],
    'scripts': ['bin/sofia']
}

setup(**config)