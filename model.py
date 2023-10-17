import torch
from transformers import pipeline
import os

model_id = os.getenv("MODEL_ID")


def load(load_only: bool = False):
    kwargs = {
        "model": model_id,
        "torch_dtype": torch.bfloat16,
        "device_map": "auto",
        "model_kwargs": {
            "low_cpu_mem_usage": True,
        },
    }

    if not load_only:
        kwargs["model_kwargs"]["use_flash_attention_2"] = True
        kwargs["model_kwargs"]["load_in_4bit"] = True

    pipe = pipeline(
        "text-generation",
        **kwargs,
    )

    return pipe
