import time
from urllib.parse import urlparse

def wait(seconds=2):
    time.sleep(seconds)

def get_domain(url:str):
    return urlparse(url).netloc