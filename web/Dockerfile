FROM tiangolo/uvicorn-gunicorn-fastapi:python3.6

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY public /app/public/
COPY ./config.py /app
COPY ./main.py /app

RUN python -m wordcookies cli --word="word" --exit # to generate dict

VOLUME /app/cache

CMD ["python", "main.py"]
