#
import requests
import json
import warnings
from urllib3.exceptions import InsecureRequestWarning

warnings.simplefilter('ignore', InsecureRequestWarning)

def try_except(url):
    try:
        data = requests.get(url, headers={"Accept": "application/json"})
        data = json.loads(data.text)
        return data
    except:
        return False


def webcheck(url):
    response = requests.get(url)

    if response.status_code == 200:
        return True
    else:
        return False

    return None
