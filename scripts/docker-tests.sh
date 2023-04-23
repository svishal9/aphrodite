docker build . -t test-aphrodite --build-arg ARG_RUN_ACTION=tests -f ./app/Dockerfile
docker run -it test-aphrodite