#!/usr/bin/env python

from setuptools import setup

setup(name='arXiv_download',
      version='0.1',
      description='View, Get Info and Download research papers from arxiv.org on your terminal!!',
      url='https://github.com/pvskand/arXiv_download',
      author='Skand Vishwanath Peri',
      author_email='pvskand@gmail.com',
      license='MIT',
      scripts=['bin/arXiv'],
      packages=['arXiv_download'],
      install_requires=[
          'docopt',
      ],
      zip_safe=False)
