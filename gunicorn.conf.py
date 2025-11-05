import multiprocessing
import os

port = int(os.getenv("PORT", "10000"))
bind = f"0.0.0.0:{port}"

workers = int(os.getenv("WEB_CONCURRENCY", str(multiprocessing.cpu_count() * 2 + 1)))
worker_class = "gthread"
threads = int(os.getenv("GTHREADS", "4"))

timeout = int(os.getenv("GUNICORN_TIMEOUT", "120"))
graceful_timeout = int(os.getenv("GUNICORN_GRACEFUL_TIMEOUT", "30"))
keepalive = int(os.getenv("GUNICORN_KEEPALIVE", "120"))

loglevel = os.getenv("GUNICORN_LOGLEVEL", "info")

