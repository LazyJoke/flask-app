FROM python:3.7

COPY . /flask-app
WORKDIR /flask-app

RUN pip install --upgrade pip
RUN pip install pipenv

CMD pipenv shell
CMD pipenv install
CMD python ../startup.py db init
CMD python ../startup.py db migrate
CMD python ../startup.py db upgrade
CMD python startup.py runserver -h 0.0.0.0 -p 10001 -D -R