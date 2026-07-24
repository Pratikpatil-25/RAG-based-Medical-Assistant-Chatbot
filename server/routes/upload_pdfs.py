from fastapi import APIRouter, UploadFile, File
from modules.load_vectorstore import load_vectorstore
from fastapi.responses import JSONResponse
from logger import logger


router=APIRouter()

# @router.post("/upload_pdfs/")
# async def upload_pdfs(files:list[UploadFile] = File(...)):
#     try:
#         logger.info("Recieved uploaded files")
#         load_vectorstore(files)
#         logger.info("Document added to vectorstore")
#         return {"messages":"Files processed and vectorstore updated"}
#     except Exception as e:
#         logger.info("Error during PDF upload")
#         return JSONResponse(status_code=500,content={"error":str(e)})

# for single file :
@router.post("/upload_pdf/")
async def upload_pdfs(file : UploadFile = File(...)):
    try:
        logger.info("Recieved uploaded file")
        load_vectorstore(file)
        logger.info("Document added to vectorstore")
        return {"messages":"File processed and vectorstore updated"}
    except Exception as e:
        logger.info("Error during PDF upload")
        return JSONResponse(status_code=500,content={"error":str(e)})