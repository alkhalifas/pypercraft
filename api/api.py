"""

"""
from fastapi import FastAPI, HTTPException, Query
from pypercraft import pypercraft
import os

app = FastAPI()

DEFAULT_API_KEY = os.getenv("OPENAI_API_KEY")


@app.get("/generate_document/")
async def generate_document(
        query: str = Query(..., title="Query", description="The query for the document."),
        topic: str = Query(..., title="Topic", description="The topic for the document."),
        num_pages: int = Query(..., title="Number of Pages", description="The total number of documents to generate."),
        api_key: str = Query(DEFAULT_API_KEY, title="API Key", description="Your API key (optional)."),
):
    if not query or not topic or num_pages <= 0:
        raise HTTPException(status_code=400, detail="Invalid input. Please provide valid query, topic, and num_pages.")

    result = pypercraft.Pypercraft(query, topic, num_pages, DEFAULT_API_KEY).construct()

    return result
