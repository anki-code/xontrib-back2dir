<p align="center">
Return to the most recently used directory when starting the xonsh shell. 
</p>

<p align="center">  
If you like the idea click ⭐ on the repo and and <a href="https://twitter.com/intent/tweet?text=Nice%20xontrib%20for%20the%20xonsh%20shell!&url=https://github.com/anki-code/xontrib-back2dir" target="_blank">tweet</a>.
</p>


## Installation

To install use pip:

```bash
xpip install xontrib-back2dir
# or: xpip install -U git+https://github.com/anki-code/xontrib-back2dir
echo "xontrib load back2dir" > ~/.xonshrc
```

## Usage

No additional actions needed. The xontrib just saves the latest directory and uses it when
xonsh starts:

```bash
bash   ~     $ xonsh
xonsh  ~     $ cd /etc
xonsh  /etc  $ exit     # the latest directory is /etc

bash   ~     $ xonsh
xonsh  /etc  $ # the latest directory
```

If you run xonsh not from the `$HOME` directory the latest directory will be ignored:

```bash
bash   ~     $ cd /tmp
bash   /tmp  $ xonsh
xonsh  /tmp  $ # latest directory ignored
```

## Links 
* This package is the part of [rc-awesome](https://github.com/anki-code/xontrib-rc-awesome) - awesome snippets of code for xonshrc in xonsh shell.
* This package is the part of [ergopack](https://github.com/anki-code/xontrib-ergopack) - the pack of ergonomic xontribs.
* This package was created with [xontrib cookiecutter template](https://github.com/xonsh/xontrib-cookiecutter).
