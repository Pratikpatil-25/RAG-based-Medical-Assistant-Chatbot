from fastapi import Request
from server.logging import logger
from fastapi.responses import JSONResponse

async def catch_exception_middleware(request: Request, call_next):
    try :
        return await call_next(request)

    except Exception as e :
        logger.info("Unhandled Exception")
        return JSONResponse(status_code=500, content={"error": str(e)})