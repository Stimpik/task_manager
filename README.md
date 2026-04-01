# Task Manager API

Простой API для управления задачами.

## Возможности

- Регистрация и аутентификация пользователей с JWT
- Создание, чтение, обновление и удаление задач
- Задачи привязаны к аутентифицированному пользователю
- База данных PostgreSQL с SQLAlchemy ORM
- Миграции через Alembic
- Автоматическая документация API (Swagger UI)

## Технологии

- **FastAPI** – веб-фреймворк
- **SQLAlchemy** – ORM
- **Alembic** – миграции
- **python-jose** – JWT
- **passlib** – хеширование паролей
- **PostgreSQL** – база данных
- **Uvicorn** – ASGI-сервер
## 📄 API Endpoints

### Аутентификация

| Метод | Эндпоинт | Описание | Тело запроса | Ответ |
|-------|----------|----------|--------------|-------|
| POST | `/auth/register` | Регистрация нового пользователя | `{"email": "user@example.com", "username": "john", "password": "secret"}` | `{"id": 1, "email": "user@example.com", "username": "john", "is_active": true, "created_at": "2025-01-01T12:00:00"}` |
| POST | `/auth/login` | Вход и получение JWT-токена | `username=john&password=secret` (form-data) | `{"access_token": "eyJ...", "token_type": "bearer"}` |

### Задачи (требуют JWT)

Все эндпоинты задач требуют передачи токена в заголовке:  
`Authorization: Bearer <your_access_token>`

| Метод | Эндпоинт | Описание | Тело запроса | Ответ |
|-------|----------|----------|--------------|-------|
| GET | `/tasks/` | Список всех задач пользователя | – | `[{"id": 1, "title": "Buy milk", "description": "Also get eggs", "completed": false, "created_at": "...", "updated_at": "...", "owner_id": 1}]` |
| POST | `/tasks/` | Создать новую задачу | `{"title": "Buy milk", "description": "Also get eggs"}` | `{"id": 1, "title": "Buy milk", "description": "Also get eggs", "completed": false, "created_at": "...", "updated_at": "...", "owner_id": 1}` |
| GET | `/tasks/{id}` | Получить детали конкретной задачи | – | `{"id": 1, "title": "Buy milk", "description": "Also get eggs", "completed": false, ...}` |
| PATCH | `/tasks/{id}` | Обновить задачу (частично) | `{"completed": true}` или `{"title": "New title"}` | Обновлённый объект задачи |
| DELETE | `/tasks/{id}` | Удалить задачу | – | `204 No Content` |
