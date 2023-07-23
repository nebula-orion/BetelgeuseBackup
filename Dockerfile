FROM python:alpine
LABEL authors="Gishant Singh"

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD [ "python", "./src/main.py" ]

