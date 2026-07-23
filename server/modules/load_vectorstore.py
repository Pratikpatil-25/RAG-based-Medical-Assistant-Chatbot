import os
import time
from pathlib import Path
from tqdm.auto import tqdm
from dotenv import load_dotenv

from pinecone import Pinecone, ServerlessSpec

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")    

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = "medical_index"
PINECONE_ENV = "us-east-1"

