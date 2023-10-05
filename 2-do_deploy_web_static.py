#!/usr/bin/python3
"""Fabric script that generates a .tgz archive"""
import os
from fabric.api import put, run, env
env.hosts = ["100.25.21.246", "54.221.183.98"]


def do_deploy(archive_path):
    """generates a .tgz archive from the contents of the web_static"""
    if not os.path.exists(archive_path):
        return False

    file = archive_path.split("/")[-1]
    name = file.split(".")[0]
    path = "/data/web_static/releases/"

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}{}".format(path, name))
        run("tar -xzf /tmp/{} -C {}{}/".format(file, path, name))
        run("rm /tmp/{}".format(file))
        run("mv {0}{1}/web_static/* {0}{1}/".format(path, name))
        run("rm -rf {}{}/wen_static".format(path, name))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(path, name))

        return True
    except:
        return False
