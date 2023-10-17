FROM python:3.10-slim

ARG MODEL_ID
ENV MODEL_ID=${MODEL_ID}

RUN apt-get update -y && apt-get install -y git

RUN pip install --upgrade pip

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY model.py .
RUN python -c "from model import load; load(True);"

COPY api.py .

CMD ["python", "api.py"]