# Выполнил: Сивцов Даниил группа №26
# Описание 
На сайте можно добовлять новости, как через бота так и через сам сайт. На сайте имеется регистрация, возможность добовлять в друзья, также имеется форум, по новостями можно оставлять комментарии, имеется система оценка новостей и комментариев. 
В самом боту реализованна авторизация, сначала идёт проверка есть ли данные о телеграм пользователе в БД. Если нет то,он отправляет данные сервису который находится в папке handler, и проверяет логин и пароль, если такой пользователь есть на сайте, то он записывает в БД телеграм айди и соответствующего ему пользователя.
Также через бота можно добавлять новости на сайт,для этого вводится последовательность данных, данные эти отправляются в тот же сервис, редактируются и на их основе добовляет новости в бд. 
В папке swager находится  restful_api которое описывает урезанные возможности сайта. А также предостпвлкн swagger интерфейс
# Домены
Доступ к сайту: http://localhost:8000/

Доступ к админке сайта: http://localhost:8000/admin

Доступк к swagger: http://localhost:8123/swagger/

Доступ к сервису: http://localhost:7000/

Телеграм бот: https://telegram.me/projectForWeb_bot

Имя бота: @projectForWeb_bot

# Запуск 
Запустить docker-compose.yml

Логин и Пароль для входа на сайт: admin

# Команды бота
/start - авторизация 

/create - создание новости

/отмена - отмена текущего действия
