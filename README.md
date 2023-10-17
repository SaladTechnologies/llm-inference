# llm-inference
A text generation inference server template for LLMs hosted by huggingface

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