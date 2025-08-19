import time
from pprint import pprint

from elasticsearch import Elasticsearch


def get_es_client(max_retries: int = 1, sleep_time: int = 5) -> Elasticsearch:
    i = 0
    while i < max_retries:
        try:
            es = Elasticsearch(
                "https://be57cce4b12743a0bf162ad1b3f98d5b.us-central1.gcp.cloud.es.io:443",
                api_key="R0tWaHI1Z0J6M0xfV3E0X3JlX286aG1IU1lKbEhSTmludWNKTlBPMUtRdw==",
                request_timeout=30
            )
            pprint("Connected to Elasticsearch!")
            return es
        except Exception:
            pprint("Could not connect to Elasticsearch, retrying...")
            time.sleep(sleep_time)
            i += 1
    raise ConnectionError("Failed to connect to Elasticsearch after multiple attempts.")
