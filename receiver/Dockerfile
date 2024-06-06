FROM python:3.9-slim
RUN pip install pika flask
COPY hello_receiver.py /hello_receiver.py
CMD ["python", "/hello_receiver.py"]
