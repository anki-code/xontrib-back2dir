import os

from pathlib import Path
from xonsh import dirstack

$XONTRIB_BACK2DIR_FILE = Path(__xonsh__.env.get('XDG_CACHE_HOME', '~/.cache')).expanduser() / 'xontrib-back2dir' / 'latest.path'

if not $XONTRIB_BACK2DIR_FILE.parent.exists():
    os.mkdir($XONTRIB_BACK2DIR_FILE.parent)

def _new_dir(newdir):
    with open($XONTRIB_BACK2DIR_FILE, 'w') as f:
        print(newdir, end='', file=f)

@events.on_chdir
def autojump_add_to_database(olddir, newdir, **kwargs):
    _new_dir(newdir)

if $PWD == $HOME and $XONTRIB_BACK2DIR_FILE.exists():
    newdir = open($XONTRIB_BACK2DIR_FILE).read()
    dirstack.cd([newdir])
