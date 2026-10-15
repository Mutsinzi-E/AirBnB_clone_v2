#!/usr/bin/python3
"""Create a .tgz archive of the web_static folder."""

from datetime import datetime
from os import makedirs
from os.path import getsize, isdir
from fabric.api import local, settings


def do_pack():
    """Create and return the archive path, or None if packing fails."""
    try:
        if not isdir("versions"):
            makedirs("versions")

        filename = "web_static_{}.tgz".format(
            datetime.now().strftime("%Y%m%d%H%M%S")
        )
        archive_path = "versions/{}".format(filename)

        print("Packing web_static to {}".format(archive_path))

        with settings(warn_only=True):
            result = local(
                "tar -czf {} web_static".format(archive_path)
            )

        if result.failed:
            return None

        print("web_static packed: {} -> {}Bytes".format(
            archive_path, getsize(archive_path)
        ))
        return archive_path

    except (OSError, IOError):
        return None
