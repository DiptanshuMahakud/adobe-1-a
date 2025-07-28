FROM --platform=linux/amd64 python:3.10-slim
 
WORKDIR /app

RUN apt-get update && apt-get install -y \
    libglib2.0-0 libxrender1 libsm6 libxext6 \
&& rm -rf /var/lib/apt/lists/*
 

COPY . .
 

RUN pip install --no-cache-dir \
    pymupdf \
    torch==2.1.0 \
    transformers==4.35.2
 

RUN mkdir -p /app/input /app/output
 

CMD ["python", "main.py"]