# This is a telegram bot for account management

## Setup Environment

### Create python environment

``` bash
pipenv install --three --python=`which python3` python-telegram-bot flask gunicorn requests
```

## Environment

Platform: Windows 10 WSL2 Ubuntu 18.04

## Quick Start

``` python
pipenv run python3 main.py
```

## Some WSL Environment Problem

The nologin is not with the path `$HOME/.local/bin`.
So we can add the lines to ~/.bashrc

``` bash
# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi
```
