from __future__ import with_statement
from fabric.api import *

env.hosts = ['128.199.237.125']

def prepare_deploy():
    local("git add . -A && git commit")
    local("git push")

def deploy():
    prepare_deploy()
    code_dir = '/home/noel/ateneodecebutk'
    with cd(code_dir):
        run("git pull")
        run("sudo service uwsgi restart")
