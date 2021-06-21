FROM python:3.7-slim

# install package libraries
RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
RUN apt-get install -y vim

ARG PROJECT=myproject
ARG PROJECT_DIR=/var/www/${PROJECT}

RUN mkdir -p ${PROJECT_DIR}
WORKDIR ${PROJECT_DIR}
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000
STOPSIGNAL SIGINT
# ENTRYPOINT ["python", "manage.py"]
# CMD ["runserver", "0.0.0.0:8000"]
ENTRYPOINT [ "bash" ]