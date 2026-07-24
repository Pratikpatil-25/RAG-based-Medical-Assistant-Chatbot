from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.ask_questions import router as ask_router
from routes.upload_pdfs import router as upload_router

# when frontend and backend run on different origins, The browser blocks it because these are different origins.
# This is called the Same-Origin Policy.
# CORS (Cross-Origin Resource Sharing) allows the backend to tell the browser: "It's okay, I trust requests coming from that origin."

from middlewares.exception_handlers import catch_exception_middleware  # This imports your custom middleware.

app = FastAPI(title="Medical Assistant API", description="API for AI Medical Assistant Chatbot")

# CORS Setup
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,    
    allow_headers=["*"],        # Allow all HTTP headers, for example: Authorization, Content-Type, Accept, Origin
    allow_methods=["*"],        # Allow every HTTP method: GET POST PUT DELETE PATCH
    allow_origins=["*"]         # Accept requests from any origin.
)

# middleware exception handler
# This tells FastAPI: "For every HTTP request, execute this middleware."
app.middleware("http")(catch_exception_middleware)
# routers

# 1. upload pdfs
app.include_router(upload_router)

# 2. asking queries
app.include_router(ask_router)




