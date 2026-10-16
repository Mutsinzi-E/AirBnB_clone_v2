#!/usr/bin/python3
"""Distribute an archive to the web servers."""

from fabric.api import env, put, run, settings
from os.path import basename, exists, join, splitext


env.hosts = ['<IP web-01>', '<IP web-02>']


def do_deploy(archive_path):
    """Deploy an archive to the web servers."""
    if not archive_path or not exists(archive_path):
        return False

    filename = basename(archive_path)
    folder = splitext(filename)[0]
    release_path = join("/data/web_static/releases", folder)
    remote_archive = join("/tmp", filename)

    try:
        with settings(warn_only=True):
            result = run("mkdir -p {}".format(release_path))
            if result.failed:
                return False

            put(archive_path, "/tmp/")

            result = run(
                "tar -xzf {} -C {}".format(
                    remote_archive, release_path
                )
            )
            if result.failed:
                return False

            result = run("rm -f {}".format(remote_archive))
            if result.failed:
                return False

            result = run(
                "mv {}/web_static/* {}/".format(
                    release_path, release_path
                )
            )
            if result.failed:
                return False

            result = run(
                "rm -rf {}/web_static".format(release_path)
            )
            if result.failed:
                return False

            result = run("rm -rf /data/web_static/current")
            if result.failed:
                return False

            result = run(
                "ln -s {} /data/web_static/current".format(
                    release_path
                )
            )
            if result.failed:
                return False

        print("New version deployed!")
        return True

    except Exception:
        return False
