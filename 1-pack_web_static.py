#!/usr/bin/python3
"""Fabric script that generates a .tgz archive"""
import os
from fabric.api import local
from datetime import datetime


def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    tgz_name = "versions/web_static_{}.tgz".format(date)

    if not os.path.exists("versions"):
        if local("mkdir versions").failed:
            return None

    if local("tar -cvzf {} web_static".format(tgz_name)).failed:
        return None

    return tgz_file
