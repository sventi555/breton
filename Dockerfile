from python:3.9.0

WORKDIR /code

RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --deploy

COPY . .

RUN chmod +x /code/collect-and-migrate.sh

CMD ["pipenv", "run", "python", "manage.py", "runserver"]
