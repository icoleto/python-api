# python-api

This is an example of a simple REST api used for educational purposes

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

It needs to have installed:

- virtualenv 1.29.9 (A tool for creating isolated virtual python environments.)
https://virtualenv.pypa.io/en/latest/installation.html

- python version: 3.6.9

### Installing
Create virtual instance with python 3.6

```bash
virtualenv --python=/usr/bin/python3.6 venv
```

Ensure the version is correct
```bash
 python --version

 #output -> Python 3.6.9
```

Install the dependencies using pip

```bash
pip install -r requirements.txt
```


### Run

Use the command:
```bash
FLASK_APP=main.py flask run

```
or
```bash
python main.py
```



## Authors

* **Iván Coleto** - [Github - icoleto](https://github.com/icoleto)
