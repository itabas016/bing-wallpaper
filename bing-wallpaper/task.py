#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: itabas <itabas016@gmail.com>
# https://github.com/itabas016/bing-wallpaper

from urllib.request import urlopen, urlretrieve
from xml.dom import minidom
import json
import os
import sys

REQUEST_URL="https://www.bing.com/HPImageArchive.aspx"
HOST="http://bing.com"
RESPONSE_OK=200
FORMAT_JSON="js"
FORMAT_XML="xml"
REGION_US="en-US"
RESOLUTION_1920x1080="1920x1080"
RESOLUTION_1366x768="1366x768"
NODE_IMAGE='image'
NODE_ENDDATE='enddate'
NODE_URL='url'
NODE_URLBASE='urlBase'
NODE_COPYRIGHT='copyright'


class Image(object):
    def __init__(self, startdate, fullstartdate, enddate, url, urlbase, copyr, copyrightlink, quiz, wp, hsh):
        self.startDate = startdate
        self.fullStartDate = fullstartdate
        self.endDate = enddate
        self.url = url
        self.urlBase = urlbase
        self.copyright = copyr
        self.copyrightLink = copyrightlink
        self.quiz = quiz
        self.wp = wp
        self.hash = hsh

def preview():
    pass

'''
Reference open source method
'''
def set_wallpaper():

    wallpaper_path = download_wallpaper()
    if wallpaper_path == '' or '.jpg' not in wallpaper_path
        print('Download wallpaper throw an error, please check error message.')
        return

    if sys.platform.startswith('win32'):
        cmd = 'REG ADD \"HKCU\Control Panel\Desktop\" /v Wallpaper /t REG_SZ /d \"%s\" /f' %wallpaper_path
        os.system(cmd)
        os.system('rundll32.exe user32.dll, UpdatePerUserSystemParameters')
        print('Wallpaper is set.')
    elif sys.platform.startswith('linux2'):
        os.system(''.join(['gsettings set org.gnome.desktop.background picture-uri file://', wallpaper_path]))
        print('Wallpaper is set.')
    else:
        print('OS not supported.')
        return
    return

def json_parse(response):
    try:
        images = json.loads(response)["images"]
        for item in images:
            image = json.loads(item, object_hook=lambda d:
                                            Image(dict['startdate'], 
                                            dict['fullstartdate'],
                                            dict['enddate'], 
                                            dict['url'], 
                                            dict['urlBase'], 
                                            dict['copyright'], 
                                            dict['copyrightlink'], 
                                            dict['quiz'], 
                                            dict['wp'], 
                                            dict['hsh']))
            filename = ''.join([image.endDate, image.urlBase.split('/')[-1]])
            img_path = os.environ['HOME'].join([filename, '.jpg'])
            if os.path.isfile(img_path):
                print('Image of', filename, 'already exsits.')
            return
            print('Downloading: ', filename)
            urlretrieve(HOST.join(url), img_path)
            return img_path

    except Exception as e:
        print('Error while processing json: ', e)
        return

def xml_parse(response):
    try:
        xmldoc = minidom.parse(response)
        for element in xmldoc.getElementsByTagName(NODE_IMAGE):

            today = element.getElementsByTagName(NODE_ENDDATE)
            url = element.getElementsByTagName(NODE_URL)
            urlBase = element.getElementsByTagName(NODE_URLBASE)
            description = element.getElementsByTagName(NODE_COPYRIGHT)

            filename = ''.join([today, urlBase.split('/')[-1]])
            img_path = os.environ['HOME'].join([filename, '.jpg'])
            if os.path.isfile(img_path):
                print('Image of', filename, 'already exsits.')
            return
            print('Downloading: ', filename)
            urlretrieve(HOST.join(url.replace('_1366x768', '_1920x1200')), img_path)
            return img_path

    except Exception as e:
        print('Error while processing XML: ', e)
        return


def download_wallpaper(idx=0, days=1, fmt=FORMAT_JSON, region=REGION_US):
    try:
        request = '%s?ids=%d&n=%d&format=%s&mkt=%s' % (REQUEST_URL, idx, days, fmt, region)
        response = urlopen(request)

        if response.status == RESPONSE_OK:
            if fmt == FORMAT_JSON:
                return json_parse(response)
            elif fmt == FORMAT_XML:
                return xml_parse(response)
            else:
                print("invaild format. only support json and xml.")
                return
        else:
            print(response.message)
            return
    except Exception as e:
        print('Error while downloading: ', idx, e)
        return  