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
        self.hsh = hsh
    

def as_object_hook(dict):
        return Image(dict['startdate'],
                     dict['fullstartdate'],
                     dict['enddate'],
                     dict['url'],
                     dict['urlbase'],
                     dict['copyright'],
                     dict['copyrightlink'],
                     dict['quiz'],
                     dict['wp'],
                     dict['hsh'])


def preview():
    try:
        img_path = download_wallpaper()
        if img_path == '' or '.jpg' not in img_path:
            print("Get wallpaper throw an error...")
        command = ''.join(['start ', img_path])
        os.system(command)
        print("The detail please check here: \r\n", img_path)
    except Exception as e:
        print("Occurred an error when open wallpaper. \r\n", str(e))

'''
Reference open source method
'''
def set_wallpaper():

    wallpaper_path = download_wallpaper()
    if wallpaper_path == '' or '.jpg' not in wallpaper_path:
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
            # image = json.loads(item, object_hook=as_object_hook)
            image = as_object_hook(item)
            filename = ''.join([image.endDate, '_', image.urlBase.split('/')[-1].lower()])
            img_path = ''.join([os.environ['USERPROFILE'], '\\', filename, '.jpg'])
            if os.path.isfile(img_path):
                print('Image of', filename, 'is already exsits.')
                return img_path
            print('Downloading: ', filename)
            urlretrieve(''.join([HOST, image.url]), img_path)
            print("Download is done~")
            print("Image file path: ", img_path)
            return img_path

    except Exception as e:
        print('Error while processing json: ', str(e))
        return

def xml_parse(response):
    try:
        xmldoc = minidom.parseString(response)
        for element in xmldoc.getElementsByTagName(NODE_IMAGE):

            today = element.getElementsByTagName(NODE_ENDDATE)[0].firstChild.nodeValue
            url = element.getElementsByTagName(NODE_URL)[0].firstChild.nodeValue
            urlBase = element.getElementsByTagName(NODE_URLBASE)[0].firstChild.nodeValue
            description = element.getElementsByTagName(NODE_COPYRIGHT)[0].firstChild.nodeValue

            filename = ''.join([today, '_', urlBase.split('/')[-1]])
            img_path = ''.join([os.environ['USERPROFILE'], '\\',filename, '.jpg'])
            if os.path.isfile(img_path):
                print('Image of', filename, 'already exsits.')
                return img_path
            print('Downloading: ', filename)
            urlretrieve(''.join([HOST, url.replace('_1366x768', '_1920x1200')]), img_path)
            print("Download is done~")
            print("Image file path: ", img_path)
            return img_path

    except Exception as e:
        print('Error while processing XML: ', str(e))
        return


def download_wallpaper(idx=0, days=1, fmt=FORMAT_JSON, region=REGION_US):
    try:
        request = '%s?ids=%d&n=%d&format=%s&mkt=%s' % (REQUEST_URL, idx, days, fmt, region)
        response = urlopen(request)

        if response.status == RESPONSE_OK:
            content = response.read().decode('utf-8')
            if fmt == FORMAT_JSON:
                return json_parse(content)
            elif fmt == FORMAT_XML:
                return xml_parse(content)
            else:
                print("invaild format. only support json and xml.")
                return
        else:
            print(response.message)
            return
    except Exception as e:
        print('Error while downloading: ', idx, str(e))
        return  