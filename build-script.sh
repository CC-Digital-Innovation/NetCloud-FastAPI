#!/bin/bash

# start api
uvicorn src.NetCloud-FastAPI:NETCLOUD_API_INST --host 0.0.0.0 --port 80 --root-path /netcloud-fastapi