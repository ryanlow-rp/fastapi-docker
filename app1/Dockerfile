FROM python:3.8-slim-buster
WORKDIR /usr/src/app

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /usr/src/app/requirements.txt

COPY . /usr/src/app

RUN chmod 777 /usr/src/app/run.sh
CMD [ "./run.sh" ]
