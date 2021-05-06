FROM python:3.7-slim

ENV PYTHONUNBUFFERED 1

RUN groupadd user && useradd --create-home --home-dir /home/user -g user user
WORKDIR /home/user/app

# Install system dependencies
RUN apt-get update && apt-get install gcc build-essential libpq-dev -y && \
    python3 -m pip install --no-cache-dir pip-tools

# install python dependencies
ADD *requirements.txt /home/user/app/
RUN pip install -r requirements.txt && \
    pip install -r dev-requirements.txt

# Clean the house
RUN apt-get purge libpq-dev -y && apt-get autoremove -y && \
    rm /var/lib/apt/lists/* rm -rf /var/cache/apt/*

ADD . /home/user/app

USER user
CMD gunicorn ecommerce.wsgi --log-file - -b 0.0.0.0:8000 --reload
