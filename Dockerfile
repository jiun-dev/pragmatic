FROM python:3.9.0

WORKDIR /home/

RUN gh repo clone jiun-dev/pragmatic

WORKDIR /home/pragmatic

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-%-)s9cdodhf%ct)zt65ayscku(gcmp57(y^s9-3#71%2773qx@" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]