# FROM continuumio/anaconda3
# COPY . /usr/app/
# EXPOSE 5000
# WORKDIR /usr/app/ 
# RUN pip install -r requirements.txt 
# RUN pip install email_validator

# ENTRYPOINT [ "python" ]

# CMD [ "run.py" ]



FROM python:3.8-slim-buster

COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
RUN pip3 install -r requirements.txt
RUN pip install email_validator

ENTRYPOINT [ "python" ]

CMD [ "run.py" ]