import requests
from flask_restful.representations import json

if __name__ == "__main__":
    files = {'file': open("./doc.py", 'rb')}
    dumps_data = json.dumps({"a": 1})
    ftp_request = requests.post(
        files=files,
        timeout=1200,
        data={'comments': dumps_data},
        url="http://localhost:10001/demo")
