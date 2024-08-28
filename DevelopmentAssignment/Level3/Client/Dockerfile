FROM python:3-alpine
WORKDIR /client
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY clientside.py .
COPY input.txt .
CMD ["python3", "clientside.py"]