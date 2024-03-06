FROM python:3.12.2-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY links links
COPY app app
COPY manage.py .

RUN SECRET_KEY=abc ./manage.py collectstatic
RUN SECRET_KEY=abc ./manage.py migrate

EXPOSE 80
CMD [ "gunicorn", "app.wsgi:application", "-b", "[::]:80" ]
