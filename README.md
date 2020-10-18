# Word Cookies

Word Cookies helper

![continuous integration](https://github.com/jojoee/wordcookies/workflows/continuous%20integration/badge.svg?branch=master)
[![PyPI version fury.io](https://badge.fury.io/py/wordcookies.svg)](https://pypi.python.org/pypi/wordcookies/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![codecov](https://codecov.io/gh/jojoee/wordcookies/branch/master/graph/badge.svg)](https://codecov.io/gh/jojoee/wordcookies)

## Usage

1. Install [Python3](https://www.python.org/downloads/) and [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

## Features

- [ ] [demo] Add cli demo gif
- [ ] [demo] Add web demo gif
- [ ] [ci] setup continuous integration
- [ ] [cd] setup continuous delivery
- [ ] [pypi] Deploy to https://pypi.org/project/wordcookies/
- [ ] [test] Add more test
- [ ] [cli] add Usage section

## Development

```
conda -V
conda deactivate
conda remove --name wordcookies --all
conda create --name wordcookies python=3.7.5
conda activate wordcookies
python -V
pip list

# dev
pip install -r requirements.txt
PYTHONPATH="$PWD" python wordcookies/cli.py
pip freeze > requirements.txt

# test
conda remove --name wordcookies_test --all
conda create --name wordcookies_test python=3.7.5
conda activate wordcookies_test
pip install -r requirements.txt
python -m flake8 --ignore=E501 wordcookies tests
python -m pytest tests --cov=./ --cov-report=xml
pip install .
python -m wordcookies cli
python -m wordcookies cli --word="word"
python -m wordcookies cli --word="word" --exit

# test pypi
pip install twine # package for publishing
python setup.py sdist bdist_wheel # build the package
```
