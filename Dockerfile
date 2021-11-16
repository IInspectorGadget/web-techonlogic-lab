# Указывает Docker использовать официальный образ python 3 с dockerhub в качестве базового образа
FROM python:3.9.4
# Устанавливает переменную окружения, которая гарантирует, что вывод из python будет отправлен прямо в терминал без предварительной буферизации
ENV PYTHONUNBUFFERED 1
# Устанавливает рабочий каталог контейнера — "app"
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
# Копирует все файлы из нашего локального проекта в контейнер
RUN pip install -r requirements.txt

ADD . /app