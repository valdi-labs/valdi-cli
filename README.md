# VALDI Command Line Interface (CLI)

The VALDI CLI is a command-line tool for interfacing with VALDI services through a terminal or command prompt.

## Installation

Install dependencies using pip.

```python
pip install -r requirements.txt
```

As usual, it is recommended to install dependencies in a Python virtualenv to avoid system-level conflicts.

## Configuration

1. Create a `.valdi` folder in the top-level directory of the codebase.
2. Create a `.env` file containing `BASE_URL=https://api.bws.xyz`.

## Usage

```
python valdi.py [-h] {configure,repository,task} ...

A command-line interface for utilizing VALDI services and managing your account.

positional arguments:
  {configure,repository,task}
    configure           Configure your account credentials
    repository          Manage your repositories
    task                Manage your computational tasks

optional arguments:
  -h, --help            show this help message and exit

```