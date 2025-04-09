Использовал Django REST Framework. БД PostgreSQL. 
Функциональные требования выполнены. 
Методы API реализованы. 
Покрытие тестами через pytest.

Запуск
1.docker compose up --build
2.по адресу http://0.0.0.0:8000/api/schema/swagger-ui/ просмотр api
3. docker exec -it <container_id> pytest main/test  для выполнения тестов при запущенном docker compose

