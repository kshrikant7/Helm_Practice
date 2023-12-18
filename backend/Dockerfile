# Dockerfile for backend
FROM python:3.7

WORKDIR /app

COPY . /app

RUN pip install flask && \
    pip install -U flask-cors
    
CMD ["python", "app.py"]