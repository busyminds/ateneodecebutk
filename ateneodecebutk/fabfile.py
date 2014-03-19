from __future__ import with_statement
from fabric.api import *

env.hosts = ['128.199.237.125']


def push():
    local("git add . -A && git commit")
    local("git push")


def pull():
    code_dir = '/home/noel/ateneodecebutk'
    with cd(code_dir):
        run("git pull")


def restart_nginx():
    run("sudo service nginx restart")


def restart_uwsgi():
    run("sudo service uwsgi restart")


def deploy():
    pull()
    restart_uwsgi()
