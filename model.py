import torch
from transformers import pipeline
from optimum.bettertransformer import BetterTransformer
import os

model_id = os.getenv("MODEL_ID")


def load(load_only=False):
    pipe = pipeline(
        "text-generation", model=model_id, torch_dtype=torch.bfloat16, device_map="auto"
    )

    if not load_only:
        pipe.to("cuda")
        pipe.model = BetterTransformer.transform(pipe.model, keep_original_model=False)

    return pipe
