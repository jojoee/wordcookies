FROM tiangolo/uvicorn-gunicorn-fastapi:python3.6

COPY public /app/public/
COPY ./requirements.txt /app/requirements.txt
COPY ./config.py /app
COPY ./main.py /app

WORKDIR /app
RUN pip install -r requirements.txt
RUN python -m wordcookies cli --word="word" --exit # to generate dict

CMD ["python", "main.py"]
