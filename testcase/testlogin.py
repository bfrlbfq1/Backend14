import  requests
class TestLogin:

    def test_login_post(self):
        r=requests.post('http://127.0.0.1:5000/login',json={
            'username':'xiaoqiang',
            'password':'456'
        })
        assert r.status_code==200
        assert r.json()['errmsg']=='ok'
        self.token = r.json()['access_token']
        return self.token
    def test_login_get(self):
        r=requests.get('http://127.0.0.1:5000/login',headers={'Authorization': f'Bearer {self.test_login_post()}'})
        print(r.json())
        assert r.status_code == 200