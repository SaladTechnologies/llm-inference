from model import load
import time
from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from enum import Enum
import uvicorn

import os

host = os.getenv("HOST", "0.0.0.0")
port = os.getenv("PORT", "1234")

port = int(port)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/hc")
async def health_check():
    return "OK"


class ChatRole(str, Enum):
    system = "system"
    user = "user"
    asssistant = "assistant"


class ChatMessage(BaseModel):
    role: ChatRole
    content: str


class LongGenerationStrategies(str, Enum):
    none = None
    hole = "hole"


class GenerationOptions(BaseModel):
    max_new_tokens: Optional[int] = 256
    do_sample: Optional[bool] = True
    top_k: Optional[int] = 50
    top_p: Optional[float] = 0.95
    temperature: Optional[float] = 0.7
    return_full_text: Optional[bool] = False
    handle_long_generation: Optional[
        LongGenerationStrategies
    ] = LongGenerationStrategies.none


class ChatRequest(BaseModel):
    messages: list[ChatMessage]
    options: Optional[GenerationOptions] = GenerationOptions()


@app.post("/chat")
async def chat(request: ChatRequest):
    if len(request.messages) < 1:
        raise HTTPException(
            status_code=400, detail="Request must contain at least one message"
        )

    start = time.perf_counter()
    prompt = pipe.tokenizer.apply_chat_template(
        request.messages, tokenize=False, add_generation_prompt=True
    )
    outputs = pipe(prompt, **request.options.model_dump())
    end = time.perf_counter()

    return {
        "outputs": outputs,
        "duration": end - start,
    }


if __name__ == "__main__":
    print("Loading model...", flush=True)
    start = time.perf_counter()
    pipe = load()
    end = time.perf_counter()
    print(f"Model loaded in {end - start:.2f} seconds", flush=True)

    uvicorn.run(app, host=host, port=port)
