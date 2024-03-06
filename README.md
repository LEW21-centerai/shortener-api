# shortener-api

Build and launch the app:

```sh
docker build -t api . && docker run -it -e DEBUG=1 -p 8000:80 api
```

Then visit http://localhost:8000/links/

## Development
You can also use Django development server:
```sh
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
DEBUG=1 ./manage.py migrate
DEBUG=1 ./manage.py runserver
```

## Deployment
See [dj12 docs](https://pypi.org/project/dj12/) for the list of environment variables you can use to configure the app's deployment.
