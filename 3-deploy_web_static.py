#!/usr/bin/python3
"""Fabric script that generates a .tgz archive"""
import os.path
from fabric.api import local, put, run, env
from datetime import datetime


env.hosts = ["100.25.21.246", "54.221.183.98"]


def do_deploy(archive_path):
    """generates a .tgz archive from the contents of the web_static"""
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True


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


def deploy():
    """generates a .tgz archive from the contents of the web_static"""
    file = do_pack()

    if not file:
        return False

    return do_deploy(file)
