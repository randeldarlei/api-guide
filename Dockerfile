FROM python:latest
WORKDIR /app
ADD ./src /app 
COPY ./requeriments.txt /etc 
RUN pip install -r /etc =/requeriments.txt 
EXPOSE 5000
CMD ["python", "python-api.py"]
