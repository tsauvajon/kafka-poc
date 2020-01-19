# Data processing pipeline using Kafka

3 components:

- new_image.py checks for new available satellite images
- cookie_cut.py downloads the images and cuts them to the shape of the fields they contain
- extract_metrics.py analyzes the cut images to extract useful info

Demo:
- Kafka (top left)
- `new_image` (bottom left)
- `cookie_cut` (middle)
- `extract_metrics` (right)

![Demo - GIF](demo.gif)

## Run

### Requirements

- Kafka 2.3.1
- Python 3.8
- pipenv, version 2018.11.26
- `pipenv install`

### Start Kafka

```sh
./start.sh
./create_topics.sh
```

### Start the pipelines

- `python new_image.py`
- `python cookie_cut.py` (suggested workers: 3)
- `python extract_metrics.py` (suggested workers: 5)
