# Base build
FROM python:3.10-alpine as builder

RUN mkdir /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# nginx
FROM nginx:1.23-alpine
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
COPY ./nginx.conf /etc/nginx/nginx.conf

# Now multistage build
FROM python:3.10-alpine
COPY --from=builder /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/
COPY . /app
WORKDIR /app
ENV PYTHONUNBUFFERED 1
EXPOSE 8080
ARG CACHEBUST=0
RUN python manage.py collectstatic
CMD ["python", "-m", "gunicorn", "--preload", "-c", "/app/config/gunicorn.py", "ecommerce.asgi:application", "-k", "uvicorn.workers.UvicornWorker"]
