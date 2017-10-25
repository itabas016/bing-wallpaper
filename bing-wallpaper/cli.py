#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: itabas <itabas016@gmail.com>
# https://github.com/itabas016/bing-wallpaper

"""
BING WALLPAPER CLI

Usage:
  bing-wallpaper preview [ <days:(days before today)> ]
  bing-wallpaper download [ <days:(days before today)> ]
  bing-wallpaper set [ <days:(days before today)> ]
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

    idx = args['-d'] if int(args['-p']) else 0

    if args["preview"] or args["p"]:
        task.preview(idx)

    elif args["download"] or args["d"]:
        task.download_wallpaper(idx)

    elif args["set"] or args["s"]:
        task.set_wallpaper(idx)

    else:
        print("unknown command for bing wallpaper.")

if __name__ == "__main__":
    main()

