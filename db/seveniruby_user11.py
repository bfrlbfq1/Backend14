from db.database import db, User


class SevenirubyUser11:
    def get_users(self):
        r = []
        for t in User.query.all():
            res = {}
            res['id'] = t.id
            res['username'] = t.username
            res['password'] = t.password
            res['email'] = t.email
            r.append(res)
        return r
        # return {'hello':'word'}

    def add_users(self, username, password,email):
        user = User.query.filter_by(username=username).first()
        if user:
            return {
                'errcode': 1,
                'errmsg': '数据存在'
            }
        else:
            try:
                print(password)
                t = User(
                    # username=request.json['username'],
                    # password=request.json['password'],
                    # email=request.json['email'],
                    username=username,
                    password=password,
                    email=email,

                )
                # print(email)
            except Exception as e:
                print(e)
            db.session.add(t)
            db.session.commit()

            return {"msk": 'ok'}

    def put_users(self, username, password, email):
        user = User.query.filter_by(username=username).first()
        # user = database.User.query.filter_by(username=username, password=password).first()
        if user:
            if password is None and email is not None:
                user.email = email
                db.session.commit()
            elif password is not None and email is None:
                user.password = password
                db.session.commit()
            elif password is not None and email is not None:
                user.password = password
                user.email = email
                db.session.commit()
        else:
            return {
                'errcode': 1,
                'errmsg': '数据更新错误'
            }
        return {
            'errcode': 0,
            'errmsg': 'ok'
        }

    def delete_users(self, username, password, email):
        print(username, password, email)
        user = User.query.filter_by(username=username).first()
        print(user)
        if user:
            db.session.delete(user)
            db.session.commit()
            return {
                'errcode': 0,
                'errmsg': f'{username}已删除'
            }
        else:
            return {
                'errcode': 1,
                'errmsg': f'{username}不存在'
            }
