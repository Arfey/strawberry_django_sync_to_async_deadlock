# strawberry_django_sync_to_async_deadlock

```
pip install -r requirements.txt

python -m gunicorn app.asgi:application -k uvicorn.workers.UvicornWorker -b 127.0.0.1:8000 
```
