import requests


def test_komedia_req():
    
    headers = {"X-API-KEY": "G22PTDH-MM6MGEQ-JJTXGTG-ZCZQBQB"}
    resp = requests.get('https://api.kinopoisk.dev/v1.4/movie?year=2023&genres.name=комедия', headers=headers)
    assert resp.status_code == 200

def test_line_req():
    
    headers = {"X-API-KEY": "G22PTDH-MM6MGEQ-JJTXGTG-ZCZQBQB"}
    resp = requests.get('https://api.kinopoisk.dev/v1.4/movie?', headers=headers)
    assert resp.status_code == 200


def test_rating_req():
    
    headers = {"X-API-KEY": "G22PTDH-MM6MGEQ-JJTXGTG-ZCZQBQB"}
    resp = requests.get('https://api.kinopoisk.dev/v1.4/movie?rating.kp=7-10', headers=headers)
    assert resp.status_code == 200   

def test_future_req():
    
    headers = {"X-API-KEY": "G22PTDH-MM6MGEQ-JJTXGTG-ZCZQBQB"}
    resp = requests.get('https://api.kinopoisk.dev/v1.4/movie?id=81-24', headers=headers)
    assert resp.status_code == 400

def test_wrong_rating_req():
    
    headers = {"X-API-KEY": "G22PTDH-MM6MGEQ-JJTXGTG-ZCZQBQB"}
    resp = requests.get('https://api.kinopoisk.dev/v1.4/movie?rating.kp=12', headers=headers)
    assert resp.status_code == 400    
