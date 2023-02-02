#!/usr/bin/python3
""" Web server distribution"""
from fabric.api import *
import os.path

env.user = 'ubuntu'
env.hosts = ['54.87.234.157', '54.160.115.69']
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Distributes archive to web servers"""
    if os.path.exists(archive_path) is False:
        return False
    try:
        arc = archive_path.split("/")
        base = arc[1].strip('.tgz')
        # upload archive
        put(archive_path, '/tmp')
        sudo('mkdir -p /data/web_static/releases/{}'.format(base))
        main = "/data/web_static/releases/{}".format(base)
        # uncompress archive and delete .tgz
        sudo('tar -xzf /tmp/{} -C {}/'.format(arc[1], main))
        sudo('rm /tmp/{}'.format(arc[1]))
        sudo('mv {}/web_static/* {}/'.format(main, main))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s {}/ "data/web_static/current"'.format(main))
        return True
    except:
        return False
