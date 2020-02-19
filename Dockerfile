FROM python:3.7
LABEL maintainer="llindstrom@lco.global"

# the exposed port must match the deployment.yaml containerPort value
EXPOSE 80
ENTRYPOINT [ "/usr/local/bin/gunicorn", "tom_demo.wsgi", "-b", "0.0.0.0:80", "--access-logfile", "-", "--error-logfile", "-", "-k", "gevent", "--timeout", "300", "--workers", "2"]

WORKDIR /tom-demo

COPY requirements.txt /tom-demo
RUN pip install --no-cache-dir -r /tom-demo/requirements.txt

COPY . /tom-demo

RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

