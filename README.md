## Bing-Wallpaper ##

_*This is a simple bing wallpaper tool, base on python language.*_

### Usage ###

You can install this package by pip ->

```python
pip install bing-wallpaper
```

or install it by local

```python
git clone git@github.com:itabas016/bing-wallpaper.git ~
python ~/bing-wallpaper/setup.py
```

### CLI Commands ###

Currently, this tool support wallpaper `preview`, `download` and `set`

```python

# preview today's wallpaper from bing website
bing-wallpaper preview

# download specify date wallpaper from bing website
# default date parameter is today, and download path is home directory
bing-wallpaper download

#set today's wallpaper to desktop
bing-wallpaper set
```