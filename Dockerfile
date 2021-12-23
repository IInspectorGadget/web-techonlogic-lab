# Указывает Docker использовать официальный образ python 3 с dockerhub в качестве базового образа
FROM python:3.9.4
# Устанавливает переменную окружения, которая гарантирует, что вывод из python будет отправлен прямо в терминал без предварительной буферизации
ENV PYTHONUNBUFFERED 1
# Устанавливает рабочий каталог контейнера — "app"

RUN mkdir /app
COPY . /app/
WORKDIR /app

RUN pip install -r requirements.txt
CMD ["python", "mysite/manage.py", "makemigrations"]
# CMD ["python", "mysite/manage.py", "migrate"]