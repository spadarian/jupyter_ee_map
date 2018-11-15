#! /usr/bin/env python
"""Simple extension of ipyleaflet Map to work with Google Earth Engine"""

from setuptools import setup, find_packages
import jupyter_ee_map

DESCRIPTION = __doc__
VERSION = jupyter_ee_map.__version__

setup(name='jupyter_ee_map',
      version=VERSION,
      description=DESCRIPTION,
      author='José Padarian',
      author_email='spadarian@gmail.com',
      url='https://github.com/spadarian/jupyter_ee_map',
      license='GPL-3.0',
      packages=find_packages(),
      zip_safe=False,
      package_data={'': ['LICENSE']},
      install_requires=['earthengine-api',
                        'ipyleaflet>=0.9.1',
                        ],
)
