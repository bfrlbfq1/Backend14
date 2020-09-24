import  requests
class TestLogin:

    def test_login_post(self):
        #登录
        r=requests.post('http://127.0.0.1:5000/login',json={
            'username':'xiaoqiang',
            'password':'456'
        })
        assert r.status_code==200
        assert r.json()['errmsg']=='ok'
        self.token = r.json()['access_token']
        return self.token
    def test_login_get(self):
        #获取用户信息
        r=requests.get('http://127.0.0.1:5000/login',headers={'Authorization': f'Bearer {self.test_login_post()}'})
        print(r.json())
        assert r.status_code == 200
    #注册
    def test_login_put(self):
        r=requests.put('http://127.0.0.1:5000/login',json={
            'username': 'xiaowang',
            'password': '456',
            'email':'ghgtyfty'
        })
        assert r.status_code==200
        assert r.json()['errmsg']=='ok'

    #删除
    def test_login_delete(self):
        r = requests.delete('http://127.0.0.1:5000/login', json={
            'username': 'xiaowang'
        })
        assert r.status_code == 200
        assert r.json()['errcode'] == 0