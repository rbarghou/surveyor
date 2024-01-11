FROM python:3.12
ENV PYTHONUNBUFFERED=1

RUN mkdir /src
WORKDIR /src

RUN apt update -y && \
    apt install -y gdal-bin

COPY requirements.txt /src
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /src

RUN mkdir /static && \
    python manage.py collectstatic --no-input

EXPOSE 8088
ENV PORT 8088
ENV PROCESSES 10

CMD uwsgi uwsgi.ini --uid 2
