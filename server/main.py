from server.logging import logger
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# when frontend and backend run on different origins, The browser blocks it because these are different origins.
# This is called the Same-Origin Policy.
# CORS (Cross-Origin Resource Sharing) allows the backend to tell the browser: "It's okay, I trust requests coming from that origin."

from server.middlewares.exception_handlers import catch_exception_middleware  # This imports your custom middleware.

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

# 2. asking queries