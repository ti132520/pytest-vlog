import requests

def test_req():
    data = {"a": 1, "b":2 }
    r = requests.post("http://127.0.0.1:8000/", json=data)
    print(r.json())