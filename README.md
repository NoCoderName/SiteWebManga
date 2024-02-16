# MangaApp

## Sources

 - [Scheme](https://miro.com/app/board/uXjVNu7G3NM=/)
 - Desig(future)
 
  # .env
 в папке проекта создать файл .env. Он добавлен в .gitgnore и не будет отслеживаться в git. в этом его основная суть.
 так же в нем находястя переменные и секреты котоыре загружаются в момент старта приложения.


   # General settings
   TIME_ZONE="Asia/Almaty"

   # PostgreSQL
   PSQL_ENGINE=postgresql
   PSQL_USER=              # pg username
   PSQL_PASSWORD=          # pg user password
   PSQL_HOST=localhost
   PSQL_NAME=              # pg db name
   PSQL_PORT=5432

*Для работы с PostgreSQl необходимо предварительно создать пользователя и базу данных