<p align="center">
Back to the latest used directory when starting xonsh shell.
</p>

<p align="center">  
If you like the idea click ⭐ on the repo and stay tuned.
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
* This package is the part of [ergopack](https://github.com/anki-code/xontrib-ergopack) - the pack of ergonomic xontribs.
* This package was created with [xontrib cookiecutter template](https://github.com/xonsh/xontrib-cookiecutter).
