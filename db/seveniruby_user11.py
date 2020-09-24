from db.database import db, User


class SevenirubyUser11:
    def get(self):
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

    def Post(self, username, password, email):
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
            print(email)
        except Exception as e:
            print(e)
        db.session.add(t)
        db.session.commit(t)

        return {"msk": 'ok'}

    def put(self, username, password, email):
        user = User.query.filter_by(username=username, password=password, email=email).first()
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

    def delete(self, username, password, email):
        user = User.query.filter_by(username=username, password=password, email=email).first()
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
