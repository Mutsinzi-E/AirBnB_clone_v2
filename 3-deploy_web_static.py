#!/usr/bin/python3
"""Create and distribute an archive to web servers."""

from fabric.api import env
from os.path import exists


env.hosts = ['<IP web-01>', '<IP web-02>']


def deploy():
    """Pack web_static and deploy the archive."""
    pack = __import__('1-pack_web_static').do_pack
    deploy_archive = __import__('2-do_deploy_web_static').do_deploy

    archive_path = pack()
    if not archive_path or not exists(archive_path):
        return False

    return deploy_archive(archive_path)
