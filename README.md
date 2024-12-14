# Система учёта заявок на ремонт

**Пользователи**
- Оператор
- Клиент
- Мастер

**Ремонт**
- Заявка на ремонт
- Регистрация заявки
- Обработка заявки
- Исполнение заявки

**Метрики (?)**
- Мониторинг и анализ

## Подготовительный этап

1. Django — фреймворк https://docs.djangoproject.com/en/5.1/
```bash
pip install Django
```

2. Создание конфигурационных файлов Django
```bash
django-admin startproject config .
```

3. Создание наших сущностей
```bash
django-admin startapp accounts
django-admin startapp repair
```

### Миграции и первый пользователь

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### Запуск проекта
```bash
python manage.py runserver
```
Остановка сервера `control + C`
