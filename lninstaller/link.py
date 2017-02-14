import shutil
import os
import datetime
from os.path import expanduser


def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)


def move_if_path_not_exists(path, target):
    pathexists = os.path.exists(path)
    targetexists = os.path.exists(target)
    if not pathexists:
        if targetexists:
            ensure_dir(path)
            shutil.move(target, path)
        else:
            raise ValueError('path ' + path + 'does not exists')


def link(path, target):
    move_if_path_not_exists(path, target)
    targetexists = os.path.exists(target)
    if targetexists:
        now = datetime.datetime.now()
        tmpfile = '/tmp/{}_{}'.format(target.replace('/', '_'), now)
        shutil.move(target, tmpfile)
    else:
        ensure_dir(target)
    os.symlink(path, target)
    print('link ' + path + ' to ' + target)


def home_link(path, target):
    home = expanduser("~")
    link(home + '/'+path, home + '/'+target)
