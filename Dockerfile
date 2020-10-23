from python:3.9.0

WORKDIR /code

COPY requirements.txt .

RUN ["pip", "install", "-r", "requirements.txt"]

COPY . .

EXPOSE 8000

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:8000", "--log-level", "warning", "main.wsgi:application"]
