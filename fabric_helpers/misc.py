def hg_pull_u(env):
    """Updates the mercurial repository."""
    with cd(env.paths.source):
        run('hg pull -u')
    
def manage_py(env, command):
    """Runs a Django manage command."""
    with cd(env.paths.source):
        run('./manage.py %s' % command)
        