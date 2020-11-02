import os

from pathlib import Path
from xonsh import dirstack

_file = Path(__xonsh__.env.get('XDG_CACHE_HOME', '~/.cache')).expanduser() / 'xontrib-back2dir' / 'latest.path'


@events.on_post_init
def on_post_init(**_):
    if Path(__xonsh__.env["PWD"]) == Path(__xonsh__.env["HOME"]).resolve() and _file.exists():
        __xonsh__.subproc_captured_stdout(['cd', _file.read_text()])

@events.on_chdir
def autojump_add_to_database(olddir, newdir, **kwargs):
    if not _file.parent.exists():
        os.mkdir(_file.parent)
    with open(_file, 'w') as f:
        print(newdir, end='', file=f)
