FROM python:3.8.10


# set environment variables
ENV DEBIAN_FRONTEND noninteractive
ENV GECKODRIVER_VER v0.31.0
ENV FIREFOX_VER 97.0
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN set -x \
   && apt update \
   && apt upgrade -y \
   && apt install -y \
            nano

# set work directory
RUN mkdir /app
WORKDIR /app

# copy files
COPY . /app/

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN chmod +x ./start_app.sh
RUN chmod +x ./wait-for-it.sh


EXPOSE 5050