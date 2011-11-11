from fabric_helpers import run

def random_tmp_file():
    """Returns the path to a random temporary file."""
    return "/tmp/%d" % randint(100000000, 10000000000000000000000)
    
def mysql_copy_db(from_env, to_env):
    """Copy a database from one env to another."""
    tmp_file = mysql_dump(from_env)
    mysql_reset_db_from_file(to_env, tmp_file)
    run("rm %s" % tmp_file)
    
def mysql_reset_db_from_file(env, file):
    """Drops, creates and the loads the content from a file into the given
    env"""
    mysql_admin(env, 'DROP DATABASE IF EXISTS %s;' % env.db.name)
    mysql_admin(env, 'CREATE DATABASE %s;' % env.db.name)
    run("mysql --default-character-set=utf8 %s < %s" %(
        env.db.info,
        file
    ))

def mysql_admin(env, command):
    """Runs a mysql command without specifying which database to run it on.
    Badly named."""
    run('mysql --default-character-set=utf8 -u%s -p%s -e "%s"' % (
        env.db.user,
        env.db.password,
        command,
    ))
    
def mysql(env, command):
    """Runs a mysql command on the given env."""
    run('mysql --default-character-set=utf8 %s -e "%s"' % (
        env.db.info,
        command,
    ))
    
def mysql_dump(env):
    """Dumps the db of the given env to a random temporary file, and returns
    path to said file."""
    tmp_file = random_tmp_file()
    run("mysqldump --default-character-set=utf8 %s > %s" % (
        envs.production.db.info,
        tmp_file,
    ))
    return tmp_file