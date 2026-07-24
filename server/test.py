from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.post("/upload")
async def upload(files: UploadFile = File(...)):
    return {"count": len(files)}