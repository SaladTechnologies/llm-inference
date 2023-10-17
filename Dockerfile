FROM python:3.10-slim

RUN apt-get update -y && apt-get install -y git

RUN pip install --upgrade pip

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY model.py .

ARG MODEL_ID
ENV MODEL_ID=${MODEL_ID}

# Only preload the model if we have a model ID 
RUN if [ -n "$MODEL_ID" ]; then python -c "from model import load; load();"; fi

COPY api.py .

CMD ["python", "api.py"]