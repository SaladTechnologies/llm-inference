FROM nvcr.io/nvidia/pytorch:23.09-py3

RUN apt-get update -y && apt-get install -y git

RUN pip install --upgrade pip

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/nightly/cu121
RUN pip install git+https://github.com/Dao-AILab/flash-attention@v2.3.2 --no-build-isolation

COPY model.py .

ARG MODEL_ID
ENV MODEL_ID=${MODEL_ID}

# Only preload the model if we have a model ID 
RUN if [ -n "$MODEL_ID" ]; then python -c "from model import load; load(True);"; fi

COPY api.py .

CMD ["python", "api.py"]