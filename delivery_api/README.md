# Delivery API

## Описание

Реализован API для оправки уведомлений

### Endpoints

`http://{ip-address}:8000/api/openapi` - Генерированное описание OpenAPI

`http://{ip-address}:8000/api/v1/send` - Отправляет уведолмление пользователю


### Формат уведомления

```json
{
  "event_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "delivery_type": "email",
  "event_type": "string",
  "template_id": "string",
  "subject": "string"
}
```

### Запуск

Сборка:

```bash
cp src/.env_example src/.env
docker-compose -f docker-compose.yml up -d
docker-compose -f docker-compose.yml down -v
```

### Описание работы

1. Endpoint получает запрос на уведомление.

2. По `user_id` получает у службы аутентификации персональные данные. Службу можно заменить на любую аналогичную, например прямого запроса в DB.

3. По `template_id` получает сгенерированное сообщение. 

4. По `delivery_type` служба отправки выбирает канал доставки. Реализовано только email, на основе базового класса легко добавить любой канал доставки.

Все службы наследуются от абстрактных классов, что дает простую возможность подстановки другого функционала.

