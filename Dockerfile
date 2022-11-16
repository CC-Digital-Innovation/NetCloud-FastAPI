FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src .

EXPOSE 80

CMD [ "uvicorn", "NetCloud-FastAPI:NETCLOUD_API_INST", "--host", "0.0.0.0", "--port", "80", "--root-path", "/netcloud-fastapi" ]