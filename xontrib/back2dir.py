import os

from pathlib import Path
from xonsh import dirstack

_file = Path(__xonsh__.env.get('XDG_CACHE_HOME', '~/.cache')).expanduser() / 'xontrib-back2dir' / 'latest.path'


@events.on_post_init
def on_post_init(**_):
    if Path(__xonsh__.env["PWD"]) == Path(__xonsh__.env["HOME"]).resolve() and _file.exists():
        d = Path(_file.read_text().strip())
        nd = d
        while not nd.exists():
            nd = nd.parent
        __xonsh__.subproc_captured_stdout(['cd', str(nd)])

@events.on_chdir
def _xontrib_back2dir(olddir, newdir, **kwargs):
    if not _file.parent.exists():
        os.mkdir(_file.parent)
    with open(_file, 'w') as f:
        print(newdir, end='', file=f)
