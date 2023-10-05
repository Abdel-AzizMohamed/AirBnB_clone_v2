#!/usr/bin/python3
"""Fabric script that generates a .tgz archive"""
import os
from fabric.api import local


env.hosts = ["100.25.21.246", "54.221.183.98"]

def do_deploy(archive_path):
    """generates a .tgz archive from the contents of the web_static"""
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if not os.path.exists(archive_path):
        return False

    if put(archive_path, "/tmp/{}".format(file)).failed:
        return False

    if run("tar -xfz /tmp/{} -C /data/web_static/releases/{}".format(file, name)).failed:
        return False

    if run("rm /tmp/{}".format(file)).failed:
        return False

    if run("rm /data/web_static/current").failed:
        return False

    if run("ln -sf /data/web_static/releases/{} /data/web_static/current".format(name)).failed:
        return False

    return True
