FROM python:3.11
LABEL maintainer="llindstrom@lco.global"

# the exposed port must match the deployment.yaml containerPort value
EXPOSE 80
ENTRYPOINT [ "poetry", "run", "gunicorn", "tom_demo_base.wsgi", "-b", "0.0.0.0:80", "--access-logfile", "-", "--error-logfile", "-", "-k", "gevent", "--timeout", "300", "--workers", "2"]

WORKDIR /tom-demo

RUN pip install --upgrade pip && pip install 'poetry >=2.0,<3.0'

COPY . /tom-demo
RUN poetry config virtualenvs.create false --local
RUN poetry lock
RUN poetry install --no-interaction

# Temporarily remove nodejs/npm from the base image until tom_nonlocalized events is installed
# # continue to setup the image with node and npm install (via nvm)
# # see https://stackoverflow.com/questions/25899912/
#
# # Use bash for subsequent RUN, CMD, ENTRYPOINT commands
# SHELL ["/bin/bash", "--login", "-c"]
#
# ENV NVM_DIR /usr/local/nvm
# RUN mkdir -p $NVM_DIR
# ENV NODE_VERSION 14.17.0
#
# # Install nvm with node and npm
# RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.38.0/install.sh | bash \
#     && source $NVM_DIR/nvm.sh \
#     && nvm install $NODE_VERSION \
#     && nvm alias default $NODE_VERSION \
#     && nvm use default
#
# ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
# ENV PATH      $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH

# write new webpack-stats.json for django-webpack-loader to use
# and install the Vue JS/CSS etc as static files
# WORKDIR /tom-demo/vue
# RUN npm install && npm run build

WORKDIR /tom-demo

RUN poetry run python manage.py collectstatic --noinput
