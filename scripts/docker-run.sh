docker build . -t run-python --build-arg ARG_RUN_ACTION=run -f app/Dockerfile
docker run -it run-python