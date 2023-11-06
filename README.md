# Word Cookies

Word Cookies helper

![continuous integration](https://github.com/jojoee/wordcookies/workflows/continuous%20integration/badge.svg?branch=master)
[![PyPI version fury.io](https://badge.fury.io/py/wordcookies.svg)](https://pypi.python.org/pypi/wordcookies/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![codecov](https://codecov.io/gh/jojoee/wordcookies/branch/master/graph/badge.svg)](https://codecov.io/gh/jojoee/wordcookies)

[![Docker Stars](https://img.shields.io/docker/stars/jojoee/wordcookies.svg?style=flat-square)](https://hub.docker.com/r/jojoee/wordcookies/)
[![Docker Pulls](https://img.shields.io/docker/pulls/jojoee/wordcookies.svg?style=flat-square)](https://hub.docker.com/r/jojoee/wordcookies/)
[![Image](https://images.microbadger.com/badges/image/jojoee/wordcookies.svg)](http://microbadger.com/images/jojoee/wordcookies)

## Demo

![Demo](https://raw.githack.com/jojoee/wordcookies/master/demo.png)
![Demo](https://i.imgur.com/xAMDvMM.gif)

## Usage

### Library

[Install](https://github.com/jojoee/wordcookies#installation) the package then

```python
from wordcookies import game
from pprint import pprint

word = "word"
chars = game.clean(word)
answers = game.get_possible_answers(chars)
g = game.group(answers)
pprint(g, width=120)

"""
{2: ['do', 'dr', 'dw', 'od', 'or', 'ow', 'rd', 'ro', 'rw', 'wd', 'wo', 'wr'],
 3: ['dor', 'dow', 'ord', 'owd', 'owr', 'rod', 'row', 'rwd', 'wod', 'wro'],
 4: ['drow', 'word']}
"""
```

### CLI

[Install](https://github.com/jojoee/wordcookies#installation) the package then

```bash
python -m wordcookies cli
python -m wordcookies cli --word="word"
python -m wordcookies cli --word="word" --exit
```

### Web (Docker)

Install [Docker](https://docs.docker.com/get-docker/) then run the [jojoee/wordcookies](https://hub.docker.com/repository/docker/jojoee/wordcookies/) Docker image by the command below

```bash
docker run -p 8082:9001 --name ctn_wordcookies jojoee/wordcookies
curl localhost:8082
```

### Web (Docker Compose)

Install [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) then

```bash
cd ./web
docker-compose -f docker-compose.yaml up
```

## Installation

```
pip install wordcookies

# or
git clone https://github.com/jojoee/wordcookies
cd wordcookies
python setup.py install
```

## Features

- [x] [demo] Add cli demo gif
- [x] [demo] Add web demo gif
- [x] [ci] setup continuous integration
- [x] [cd] setup continuous delivery
- [x] [pypi] Deploy to https://pypi.org/project/wordcookies/
- [ ] [test] Add more test
- [x] [cli] add Usage section
- [ ] [web][docker] use Python base image instead of current
- [ ] [web][docker] generate dict while building a Docker image
- [x] [web] add web version
- [x] [web][docker] add Docker support
- [x] [web][cache] with file and Redis
- [ ] [web][cache] pre-caching most common word
- [x] [web] enhance UI
- [x] [dict] using nltk data is not good enough, so need to combine with "ahmadly/WordCookiesCheat" (you can try with beginner level, some word is missing)
- [ ] [web] add e2e test
- [ ] [web] compress data when saving into Redis

## Development

```bash
conda -V
conda deactivate
conda remove --name wordcookies --all
conda create --name wordcookies python=3.7.5
conda activate wordcookies
python -V
pip list

# lib, dev
pip install -r requirements.txt
PYTHONPATH="$PWD" python wordcookies/cli.py
pip freeze > requirements.txt

# lib, test
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

# lib, test pypi
pip install twine # package for publishing
python setup.py sdist bdist_wheel # build the package

# web
cd ./web
conda remove --name wordcookies_web --all
conda create --name wordcookies_web python=3.7.5
conda activate wordcookies_web
pip install -r requirements.txt
uvicorn main:app --reload --port 9002 # dev + hot reload
uvicorn main:app --port 9002 & # dev
python main.py # run on prod

# web, util
lsof -i -n -P | grep 9002
docker run -p 6379:6379 --name ctn_redis -d redis:6.0.8

# web, Cocker
cd ./web
docker build -f Dockerfile -t jojoee/wordcookies:dev .
docker run -p 8082:9001 --name ctn_wordcookies jojoee/wordcookies:dev
docker run -p 8082:9001 --name ctn_wordcookies jojoee/wordcookies
docker start ctn_wordcookies
http://localhost:8082/healthcheck
http://localhost:8082/404

# web, Docker Compose
docker-compose -f docker-compose.yaml up
docker-compose -f docker-compose.dev.yaml up --build
docker-compose -f docker-compose.dev.yaml up
```

## Reference
- [Word Cookies!®](https://play.google.com/store/apps/details?id=com.bitmango.go.wordcookies&hl=en)
- [Word Cookies!®](https://itunes.apple.com/us/app/word-cookies/id1153883316?mt=8)
- https://github.com/ahmadly/WordCookiesCheat
- Data for building word dictionary
  - https://www.nltk.org/nltk_data/
  - https://github.com/ahmadly/WordCookiesCheat
  - https://www.nltk.org/data.html
  - https://github.com/dwyl/english-words
  - https://stackoverflow.com/questions/2213607/how-to-get-english-language-word-database
