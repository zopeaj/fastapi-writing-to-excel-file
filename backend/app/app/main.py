import os
import sys

path = os.environ['FILE_PATH']
sys.path.append(path)

from fastapi import FastAPI
from app.api.routes import api_router

app = FastAPI(title="", openapi_url="")

app.include_router(api_router, prefix="")
