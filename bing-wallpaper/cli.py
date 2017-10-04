#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: itabas <itabas016@gmail.com>
# https://github.com/itabas016/bing-wallpaper

"""
BING WALLPAPER CLI

Usage:
  bing-wallpaper preview
  bing-wallpaper download
  bing-wallpaper set
  bing-wallpaper -h | --help
  bing-wallpaper -V | --version

Subcommands:
  preview       preview bing wallpaper
  download      download wallpaper to local(default folder: ~)
  set           set wallpaper to desktop

Options:
  -h, --help          Help information
  -V, --version       Show version
"""


from docopt import docopt
import task

def main(args=None):

    if not args:
        args = docopt(__doc__, version="bing-wallpaper {0}".format(__version__))

    if args["preview"] or args["p"]:
        task.preview()

    elif args["download"] or args["d"]:
        task.download_wallpaper()

    elif args["set"] or args["s"]:
        task.set_wallpaper()

    else:
        print("unknown command for bing wallpaper.")

if __name__ == "__main__":
    main()

