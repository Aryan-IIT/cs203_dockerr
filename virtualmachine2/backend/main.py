from fastapi import FastAPI
import requests

app = FastAPI()

# Elasticsearch endpoint for document operations
ES_URL = "http://es:9200/my_index/_doc/"

@app.post("/insert")
def add_document(document: dict):
    """Inserts a document into Elasticsearch."""
    response = requests.post(ES_URL, json=document)
    return response.json()

@app.get("/get")
def fetch_documents():
    """Retrieves all documents from Elasticsearch."""
    print("Received GET request")
    response = requests.get(ES_URL + "_search", json={"query": {"match_all": {}}})
    return response.json()

