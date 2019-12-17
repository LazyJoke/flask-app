FROM python:3.7.5

ENV ROOT_DIR /web

ADD app $ROOT_DIR/app
ADD shell $ROOT_DIR/shell
ADD Pipfile* $ROOT_DIR/
ADD startup.py $ROOT_DIR/
ADD requirements.txt $ROOT_DIR/

WORKDIR $ROOT_DIR

RUN pip install --upgrade pip && pip install -r requirements.txt
RUN chmod a+x ./shell/migrate.sh

CMD python startup.py runserver -h 0.0.0.0 -p 10001 -D -R

EXPOSE 10001