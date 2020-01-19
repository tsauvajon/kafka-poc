#
# When a new image is available, extract useful info from it
#

import json
from time import sleep

from conf import config
from fake_data import field_names
from topics import image_ready_topic

from kafka import KafkaConsumer, KafkaProducer


kafka_url = config['kafka']['url']
min, max = config['nb']['min_fields_in_tile'], config['nb']['max_fields_in_tile']
extract_metrics_duration = config['duration']['extract_metrics']

consumer = KafkaConsumer(
    image_ready_topic, bootstrap_servers=kafka_url, group_id='metrics_pipeline')
producer = KafkaProducer(bootstrap_servers=kafka_url)

print('waiting for new field images...')
for msg in consumer:
    payload = json.loads(msg.value)

    print(
        f'image_ready -> {payload["id"]}/{payload["field"]}: extracting metrics...')
    sleep(extract_metrics_duration)
    print(f'OK')
