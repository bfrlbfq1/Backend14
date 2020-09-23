import requests
import datetime
import random
def test_seveniruby_user11_get():
    r= requests.get('http://127.0.0.1:5000/db')
    assert r.status_code==200

def test_seveniruby_user11_post():
    r= requests.post('http://127.0.0.1:5000/db',json={
        'id':random.randint(4,999),
        'username': f'name {str(datetime.datetime.now())}',
        'password': 'd',
        'email': 'fdsggd'
    })
    assert r.status_code==200
    assert r.json()['msg']=='ok'