FROM python:3
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
CMD ["gunicorn", "practicaDjangoG1.wsgi", "-b 0.0.0.0:8000"]