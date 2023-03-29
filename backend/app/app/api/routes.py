import os
import sys

path = os.environ['FILE_PATH']
sys.path.append(path)


from fastapi import APIRouter
from app.api.controller.ExcelController import excelroutes

api_router = APIRouter()
api_router.include_router(excelroutes, prefix="", tags=[""])

