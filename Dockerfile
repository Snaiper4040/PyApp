FROM python:3.8-slim-buster
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
EXPOSE 5000
RUN ["python", "test_app.py"]
CMD ["python", "app.py"]
