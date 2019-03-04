FROM python:3.6
ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

ADD . /sample
WORKDIR /sample
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD bash -c "python manage.py migrate && gunicorn --timeout 300 -b :8080 wsgi"
