#!/usr/bin/python3
"""module that generates zip file"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """class that compresses the web_static files to archive"""
    time_fmt = '%Y%m%d%H%M%S'
    time_string = datetime.now().strftime(time_fmt)
    archive = 'versions/web_static_{}.tgz'.format(time_fmt)
    local('mkdir -p versions')
    result = local('tar -czvf {} web_static'.format(archive))
    if result.failed:
        return None
    else:
        return archive
