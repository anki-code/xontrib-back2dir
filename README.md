<p align="center">
Back to directory.
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

No additional actions needed. The xontrib just save the last used directory:

```bash
bash   ~     $ xonsh
xonsh  ~     $ cd /etc
xonsh  /etc  $ exit     # the last used directory is /etc

bash   ~     $ xonsh
xonsh  /etc  $ # last used directory
```

## Credits

This package was created with [xontrib cookiecutter template](https://github.com/xonsh/xontrib-cookiecutter).
