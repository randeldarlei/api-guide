FROM python:latest
WORKDIR /app
ADD ./src /app 
COPY requirements.txt ./
RUN pip install -r requeriments.txt 
EXPOSE 5000
CMD ["python", "python-api.py"]
