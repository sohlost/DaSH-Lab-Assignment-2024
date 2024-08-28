FROM python:3-alpine
WORKDIR /server
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY serverside.py .
CMD ["python3", "serverside.py"]