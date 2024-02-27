#!/usr/bin/python3

from fabric import task, Connection
from fabric.api import run, lo

@task
def run(c):
    with Connection('ubuntu@54.152.133.156') as conn:
        result = conn.run('cat ~/commit', pty=True)
        print(result.stdout)
