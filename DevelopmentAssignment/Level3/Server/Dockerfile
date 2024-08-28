FROM python:3-alpine
WORKDIR /server
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV OPENAI_API_KEY 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
COPY serverside.py .
EXPOSE 5000
CMD ["python3", "serverside.py"]
