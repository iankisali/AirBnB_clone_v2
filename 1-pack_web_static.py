#!/usr/bin/python3
from fabric.api import local
from time import strftime
from datetime import date


def do_pack():
    """ A script generating archive the contents of web_static folder"""
    dates = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/".format(dates))
        return "versions/web_static_{}.tgz".format(dates)

    except Exception as e:
        return None
