#!/usr/bin/python3

from fabric import task, Connection

@task
def run():
    with Connection('ubuntu@54.152.133.156') as c:
        result = c.run('ls -l ~/', pty=True)
        print(result.stdout)
