FROM python:3.10

WORKDIR /opt/src/genie_project

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /opt/src/genie_project/requirements.txt
RUN chmod +x /opt/src/genie_project/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /opt/src/genie_project
