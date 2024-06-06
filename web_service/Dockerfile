FROM python:3.9-slim
WORKDIR /app
COPY app.py /app
RUN apt-get update && pip install flask requests
CMD ["python", "app.py"]
