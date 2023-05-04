#!/usr/bin/python3
"""module that deploys the archive to the web server"""
from fabric.api import *
from os.path import exists

env.hosts = ['174.129.68.202', '100.26.53.81']

def do_deploy(archive_path):
    """deploying archives to web servers"""
    if not exists(archive_path):
        return False
    filename  = archive_path,split("/")[-1]
    no_extra = filename.split(".")[0]
    put(archive_path, "/tmp")
    run("mkdir -p /data/web_static/releases/{}".format(no_extra))
    run("tar -xzf /tmp/{} -C /data/web_static/releases/".format(filename, no_extra))
    run("rm /tmp/{}".format(filename))
    run("mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}".format(no_extra, no_extra))
    run("rm -fr /data/web_static/releases/{}/web_static/".format(no_extra))
    run("rm -rf /data/web_static/current")
    run("ln -s /data/web_static/releases/{}/ \
            /data/web_static/current".format(no_extra))
    print("New version deployed!")
    return True
