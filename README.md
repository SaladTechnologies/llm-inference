# llm-inference
A text generation inference server template for LLMs hosted by huggingface

## Discover compatible models

```bash
# Syntax: models [--task <task>] [--limit <limit>]
#   --task: The task to search for. Defaults to "text-generation"
#   --limit: The number of models to show. Defaults to 100

./models --limit 500
```

This script will let you search compatible models on huggingface hub, and copies your selection the clipboard

## Build

You can bake a model into the image by supplying a model id to the build script. The model will be downloaded and cached in the image. The model will be loaded into memory when the container starts.

```bash
./build HuggingFaceH4/zephyr-7b-alpha
```

Alternatively, you can build and use the base image, and specify your model id at runtime. This will download the model when the container starts.

```bash
./build
```

## Run

Modify the docker-compose.yml file to select your model, port, and host.

```bash
docker compose up
```