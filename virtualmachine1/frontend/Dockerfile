FROM python:slim
WORKDIR /app
COPY requirements.txt .
# install requirements
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9567"]
