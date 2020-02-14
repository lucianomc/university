FROM python

WORKDIR /usr/src/app

RUN apt update -y

RUN pip install pipenv

EXPOSE 8000

ENTRYPOINT [ "bash" ]
