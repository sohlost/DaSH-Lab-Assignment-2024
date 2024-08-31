FROM python:3-alpine
WORKDIR /server
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV OPENAI_API_KEY <your-openai-key>
COPY serverside.py .
EXPOSE 5000
CMD ["python3", "serverside.py"]
