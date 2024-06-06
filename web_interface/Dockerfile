FROM python:3.9-slim
RUN pip install flask
COPY web_interface.py /web_interface.py
COPY index.html /index.html
CMD ["python", "/web_interface.py"]
