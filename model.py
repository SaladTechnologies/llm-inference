import torch
from transformers import pipeline
import os

model_id = os.getenv("MODEL_ID")


def load():
    pipe = pipeline(
        "text-generation",
        model=model_id,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        low_cpu_mem_usage=True,
        use_flash_attention_2=True,
        load_in_8_bit=True,
    )

    return pipe
