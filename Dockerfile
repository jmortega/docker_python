FROM python:3.6
MAINTAINER user "user@email.com"
RUN groupadd -r userpython && useradd -r -g userpython userpython
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
USER userpython
CMD [ "python", "app.py" ]
