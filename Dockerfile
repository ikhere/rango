FROM python:2.7
ENV PYTHONUNBUFFERED 1
WORKDIR /opt
RUN git clone https://github.com/DamnWidget/anaconda.git -b docker
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
