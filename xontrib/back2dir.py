import os

from pathlib import Path
from xonsh import dirstack

_file = Path(__xonsh__.env.get('XDG_CACHE_HOME', '~/.cache')).expanduser() / 'xontrib-back2dir' / 'latest.path'

if not _file.parent.exists():
    os.mkdir(_file.parent)

if __xonsh__.env["PWD"] == __xonsh__.env["HOME"] and _file.exists():
    with open(_file) as f:
        newdir = f.read()
    dirstack.cd([newdir])

@events.on_chdir
def autojump_add_to_database(olddir, newdir, **kwargs):
    with open(_file, 'w') as f:
        print(newdir, end='', file=f)
