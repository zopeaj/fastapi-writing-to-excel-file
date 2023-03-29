import os
import sys

path = os.environ['FILE_PATH']
sys.path.append(path)

from fastapi import APIRouter
from fastapi.requests import Request
from app.core.business.abstracts.ExcelService import ExcelService


excelService = ExcelService()
excelroutes = APIRouter()

@excelroutes.post("/")
def write_data_to_excel(request: Request):
    return excelService.writeToExcelFile(None)

@excelroutes.get("/")
def get_excel_file(request: Request):
    return excelService.readExcelFile(None)


