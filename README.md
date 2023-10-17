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

## Use

```bash
curl  -X POST \
  'http://localhost:1234/chat' \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful AI assistant. You strive for accuracy and usefulness. You only answer in rhyming iambic pentameter couplets."
    },
    {
      "role": "user",
      "content": "How was pizza invented?"
    }
  ],
  "options": {
    "max_new_tokens": 1024
  }
}' | jq -r '.outputs[0].generated_text'
```

Output:
```text
In Naples, a master did bake
A flatbread with tomato and bake
The sauce was a simple mix
Of canned tomatoes and olive's slick

The cheese, mozzarella, was added
To give it a flavor that was jaded
The result was a dish so divine
That people couldn't resist the sign

From Naples, it traveled the world
And pizza became the world's swirl
A dish for all to enjoy
That's how pizza's history was sowed.

So, the next time you eat a slice
Of pizza, take a moment to reminisce
On how a simple flatbread transformed
Into a dish that we all adore.
```