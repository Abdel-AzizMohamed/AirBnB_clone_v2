#!/usr/bin/python3
"""Fabric script that generates a .tgz archive"""
from 1-pack_web_static import do_pack
from 2-do_deploy_web_static import do_deploy
env.hosts = ["100.25.21.246", "54.221.183.98"]


def deploy():
    """generates a .tgz archive from the contents of the web_static"""
    file = do_pack()

    if not file:
        return False

    return do_deploy(file)
