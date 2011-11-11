from fabric.api import run as fab_run, sudo as fab_sudo
from fabfile import DEBUG

def run(cmd):
    """Runs a nicely niced run command, or prints it if DEBUG is on."""
    cmd = 'nice -n 19 %s' % cmd
    if DEBUG == False:
        return fab_run(cmd)
    else:
        print "run: %s" % cmd

def sudo(cmd):
    """Runs a nicely niced sudo command, or prints it if DEBUG is on."""
    cmd = 'nice -n 19 %s' % cmd
    if DEBUG == False:
        return fab_sudo(cmd)
    else:
        print "sudo: %s" % cmd