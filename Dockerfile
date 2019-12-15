FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /team-manager
WORKDIR /team-manager
ADD requirements.txt /team-manager/
RUN pip install -r requirements.txt
ADD . /team-manager/