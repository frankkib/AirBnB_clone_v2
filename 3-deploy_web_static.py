#!/usr/bin/python3
"""module for deploying web"""
from fabric.api import env, local, put, run
from datetime import datetime
import os

env.hosts = ['174.129.68.202', '100.26.53.81']
env.user = '<ubuntu'
env.key_filename = '~/id_rsa'


def do_pack():
    """"function that packs the web"""
    try:
        os.makedirs("versions")
    except:
        pass
    file_name = "versions/web_static_{}.tgz"\
            .format(datetime.now().strftime("%Y%m%d%H%M%S"))
    local("tar -cvzf {} web_static".format(file_name))
    return file_name if os.path.exists(file_name) else None


def do_deploy(archive_path):
    """function that deploys the web_static into web servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        folder_name = "/data/web_static/releases/{}"\
                .format(file_name.split(".")[0])
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}/".format(folder_name))
        run("sudo tar -xzf /tmp/{} -C {}/".format(file_name, folder_name))
        run("sudo rm /tmp/{}".format(file_name))
        run("sudo mv {}/web_static/* {}/".format(folder_name, folder_name))
        run("sudo rm -rf {}/web_static".format(folder_name))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(folder_name))
        return True
    except:
        return False


def deploy():
    """"function that deploys the web_static into web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
