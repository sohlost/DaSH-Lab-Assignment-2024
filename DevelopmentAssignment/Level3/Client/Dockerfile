FROM python:3-alpine
WORKDIR /client
COPY clientside.py .
COPY input.txt .
ENV HOSTNAME promptserver
CMD ["python3", "clientside.py", "1", "input.txt"]
