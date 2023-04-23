ARG PYTHON_VERSION=3.10.8
FROM python:$PYTHON_VERSION
USER root
WORKDIR /opt
RUN pip3 install pipenv
#TODO : Change the user to non root user
#USER 185
WORKDIR /app
COPY ../Pipfile Pipfile.lock setup.cfg /app/
COPY ../go.sh /app/go.sh
COPY ../scripts /app/scripts
RUN ./go.sh setup
COPY ./app/com /app/com
COPY ./app/__init__.py /app/__init__.py
ARG ARG_RUN_ACTION
ENV RUN_ACTION=$ARG_RUN_ACTION
#ENV RUN_ACTION=demo
ENTRYPOINT exec ./go.sh $RUN_ACTION
