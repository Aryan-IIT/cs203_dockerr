from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import requests
import os

app = FastAPI()

# Set backend URL from environment variable or default to localhost
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

@app.get("/", response_class=HTMLResponse)
def home():
    """Serve the homepage with a simple UI for Elasticsearch document management."""
    return """
    <html>
    <head><title>FastAPI Frontend</title></head>
    <body>
        <h2>Elasticsearch Document Manager</h2>
        <textarea id="inputText" placeholder="Enter text" style="width:500px;height:150px;"></textarea><br>
        <button onclick="insertDocument()">Insert</button>
        <button onclick="getDocument()">Get Best Document</button>
        <div id="output" style="margin-top:20px;"></div>
        <script>
            function insertDocument() {
                const text = document.getElementById("inputText").value;
                fetch("/insert", {
                    method: "POST",
                    headers: {"Content-Type": "application/json"},
                    body: JSON.stringify({text: text})
                })
                .then(response => response.text())
                .then(data => document.getElementById("output").innerText = data);
            }
            function getDocument() {
                fetch("/get")
                .then(response => response.json())
                .then(data => document.getElementById("output").innerText = data.text || "No documents found");
            }
        </script>
    </body>
    </html>
    """

@app.get("/get")
def fetch_document():
    """Fetch a document from the backend service."""
    response = requests.get(f"{BACKEND_URL}/get")
    print("Received GET request")
    print(response, "\n")
    return response.json()

@app.post("/insert")
def add_document(doc: dict):
    """Send a document to be inserted into the backend."""
    response = requests.post(f"{BACKEND_URL}/insert", json=doc)
    return response.json()

