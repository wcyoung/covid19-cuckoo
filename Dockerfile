FROM python:3.8.5

ENV TZ=Asia/Seoul

WORKDIR /app

RUN pip install pipenv
RUN pipenv sync

CMD ["pipenv", "run", "start"]
