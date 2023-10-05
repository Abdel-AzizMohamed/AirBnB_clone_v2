#!/usr/bin/python3
"""Fabric script that generates a .tgz archive"""
import os
from fabric.api import local
from datatime import datetime


def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    date = datetime.utcnow()
    tgz_name = "versions/web_static_{}{}{}{}{}{}".format(date.year, date.month,
                                                         date.day, date.hour,
                                                         date.minute,
                                                         date.second)
    if not os.path.exists("versions"):
        if local("mkdir versions").failed:
            return None

    if local("tar -cvfz {} web_static".format(tgz_name)).failed:
        return None

    return tgz_file
