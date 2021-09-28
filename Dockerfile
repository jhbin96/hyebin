FROM python:3.9.0

WORKDIR /home/

RUN echo 'adfhjkguk'

RUN git clone https://github.com/jhbin96/hyebin.git

WORKDIR /home/hyebin/


RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=ai_practice2.settings.deploy && python manage.py migrate --settings=ai_practice2.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=ai_practice2.settings.deploy ai_practice2.wsgi --bind 0.0.0.0:8000"]