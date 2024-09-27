import requests


headers = {"X-API-KEY": "G22PTDH-MM6MGEQ-JJTXGTG-ZCZQBQB"}


def test_komedia_req():
    
    
    resp = requests.get('https://api.kinopoisk.dev/v1.4/movie?year=2023&genres.name=комедия', headers=headers)
    assert resp.status_code == 200
    assert resp.json()['docs'][0]['alternativeName'] == 'Dad Jokes'
def test_line_req():
    
    
    resp = requests.get('https://api.kinopoisk.dev/v1.4/movie?', headers=headers)
    assert resp.status_code == 200


def test_rating_req():
    
    
    resp = requests.get('https://api.kinopoisk.dev/v1.4/movie?rating.kp=7-10', headers=headers)
    assert resp.status_code == 200
    assert resp.json()['docs'][0]['ageRating'] == 18   

def test_future_req():
    
    
    resp = requests.get('https://api.kinopoisk.dev/v1.4/movie?id=81-24', headers=headers)
    assert resp.status_code == 400
    assert resp.json()['message'][0] == 'Значение поля id должно быть в диапазоне от 250 до 7000000!'

def test_wrong_rating_req():
    
    
    resp = requests.get('https://api.kinopoisk.dev/v1.4/movie?rating.kp=12', headers=headers)
    assert resp.status_code == 400    
