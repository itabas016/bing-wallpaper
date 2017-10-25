#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: itabas <itabas016@gmail.com>
# https://github.com/itabas016/bing-wallpaper

from distutils.core import setup
from setuptools import setup, find_packages
import io, os, re

def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

with open("requirements.txt") as f:
    requires = [l for l in f.read().splitlines() if l]

setup(name='bing-wallpaper-itabas',
      version=find_version("bing-wallpaper", "__init__.py"),
      description='Bing Wallpaper tool by itabas',
      author='itabas',
      author_email='itabas016@gmail.com',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=find_packages(),
          install_requires=requires,
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
     )