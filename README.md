# Тестовое задание от IT Solution

Делаем скрипт для создания видео бегущей строки

## Запуск

**Предварительные требования**
- Docker

**Шаги**
1. Клонирование репозитория:

   ```sh
   git clone https://github.com/Aren2020/test-task-IT-Solution.git
   cd test-task-IT-Solution
   ```

2. Создать свой `.env` file (пример файла):

   ```sh
   DEBUG=0
   SECRET_KEY=YOUR_SECRET_KEY
   DJANGO_ALLOWED_HOSTS=* 
   POSTGRES_DB=postgres
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   REDIS_HOST=redis
   REDIS_PORT=6379
   REDIS_DB=0
   ```
   
4. Сборка Docker образа:
   ```sh
   docker-compose build
   ```

5. Запуск Docker контейнеров:

   ```sh
   docker-compose up
   ```

6. Применение миграций:

   ```sh
   docker-compose exec web python manage.py migrate
   ```

7. Доступ к приложению: Откройте веб-браузер и перейдите по адресу `http://localhost:80`.


## От себя

Благодарю за предоставленное тестовое задание. Готов ответить на вопросы и обсудить детали дальнейших шагов.

`aren.allahverdyan@gmail.com`

`https:/t.me/arenallahverdyan`