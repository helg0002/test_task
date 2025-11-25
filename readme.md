# FastAPI Contacts Service

Сервис для управления лидами, источниками и операторами с распределением по весам.

---

##  Локальный запуск

### 1. Установить зависимости
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Запустить сервер
```bash
uvicorn main:app --reload
```


##  Запуск через Docker

### 1. Собрать образ
```bash
docker build -t fastapi-contacts .
```
### 2. Запустить контейнер
```bash
docker run -d \
  --name fastapi_app \
  --restart always \
  --env-file .env \
  -p 5000:5000 fastapi-contacts
```

