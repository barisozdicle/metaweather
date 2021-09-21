FROM python:3.7

ADD ./ /Weather
WORKDIR /Weather

RUN pip3.7 install -r ./requirements.txt
ENV PYTHONPATH /Weather

CMD [ "python", "app/test.py" ]