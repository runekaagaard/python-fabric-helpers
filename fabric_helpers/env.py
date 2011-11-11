from fabric.state import _AttributeDict
from fabfile import safe_env_names, envs

def adict(**kwargs):
    """Returns a fabric _AttributeDict that you can query as an object, to 
    avoid using the ['foo'] bore. It allows for creating all envs like:
    
        envs = adict(
            production = adict(
                name = 'production',
                user = 'username',
                hosts = ['domain.com'],
                db = dbdict(
                    name = 'db_name',
                    user = 'user',
                    password = 'pass',
                    info = '-u%s -p%s %s',
                    path_backup = '/some/path',
                ),
                paths = adict(
                    source = '/some/path',
                    documentation = '/some/path',  
                ),
                restart_web_server_command = 'supervisorctl restart domain.com'
            ),
            testing = adict(
                ... similar to "production".
                
    If you want a access a setting from a specific env, you can the do something
    like:
    
        envs.production.db.name
    """
    return _AttributeDict(dict(**kwargs))

def dbdict(**kwargs):
    """Special adict that formats info with db name, user and password info for
    use with mysql and mysqldump commands."""
    the_dict = _AttributeDict(dict(**kwargs))
    the_dict.info = the_dict.info % (the_dict.user, the_dict.password, 
                                     the_dict.name)
    return the_dict

def assert_safe_env():
    """Exits if we are not in a safe environment."""
    assert env.name in safe_env_names, "Not a safe environment."
     
def select_env(env_name):
    """Sets current env - see adict()."""
    assert env_name in envs, "Environment does not exist."
    for k,v in envs[env_name].iteritems():
        setattr(env, k, v)
    