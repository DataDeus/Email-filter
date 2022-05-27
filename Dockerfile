FROM python:3.8-slim-buster

RUN pip3 install nltk

RUN [ "python", "-c", "import nltk; nltk.download('all')" ]

WORKDIR /root

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python", "./filter.py" ]