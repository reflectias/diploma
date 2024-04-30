FROM python:3.9

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN apt-get update && apt-get install -y 

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

CMD ["python", "app.py"]