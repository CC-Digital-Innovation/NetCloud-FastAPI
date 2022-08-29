FROM python:3.10-slim

# install curl and jq
RUN apt-get update && apt-get install -y curl jq

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

CMD [ "./build-script.sh" ]