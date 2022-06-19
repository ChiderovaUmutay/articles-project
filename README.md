# article_project

## Зависимости:
Для запуска проекта установить Python версии 3.7 и выше и pip

## Локальный запуск проекта:
После клонирования проекта выполните косманды:

### Создайте виртуальное окружение командой:
```bash
python -m venv venv
```
### Активируйте виртуальное окружение командой:
```bash
sourse venv/bin/activate
venv\Scripts\activate
```

### Установите зависимости командой:
```bash
pip instull -r requirements.txt
```

### Перейдите в папку source командой:
```bash
cd source
```

### Примените миграции командой:
```bash
python manage.py migrate
```

### Запустите проект командой:
```bash
python manage.py runserver
```

### Cоздайте администратора командой:
```bash
python manage.py createsuperuser
```

### Для доступа в панель администратора перейдите по ссылке http://localhost:8000/admin


