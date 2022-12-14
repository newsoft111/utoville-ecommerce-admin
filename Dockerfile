# python 버전 or latest 입력
FROM python:3.11.0

ENV PYTHONUNBUFFERED 1

RUN apt-get -y update
RUN apt-get -y install vim


RUN mkdir /var/django
ADD . /var/django

WORKDIR /var/django

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry export -f requirements.txt > requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8002
# django를 단독으로 실행할때 사용 명령어
# 단, nginx를 이용해서 django를 실행
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]

# guinicorn를 이용해서 django를 실행할때 사용
CMD ["gunicorn", "--bind", "0:8002", "config.wsgi:application"]