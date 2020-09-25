from db.database import db, TestReport


class SevenirubyTestreport:
    def get_report(self):
        r = []
        for t in TestReport.query.all():
            res = {}
            res['id'] = t.id
            res['reportname'] = t.reportname
            res['description'] = t.description
            res['data'] = t.data
            r.append(res)
        return r
        # return {'hello':'word'}

    def add_report(self, reportname, description,data):
        user = TestReport.query.filter_by(reportname=reportname).first()
        if user:
            return {
                'errcode': 1,
                'errmsg': '数据存在'
            }
        else:
            try:
                print(description)
                t = TestReport(
                    # reportname=request.json['reportname'],
                    # description=request.json['description'],
                    # data=request.json['data'],
                    reportname=reportname,
                    description=description,
                    data=data,

                )
                # print(data)
            except Exception as e:
                print(e)
            db.session.add(t)
            db.session.commit()

            return {"msk": 'ok'}

    def put_report(self, reportname, description, data):
        user = TestReport.query.filter_by(reportname=reportname).first()
        # user = database.TestReport.query.filter_by(reportname=reportname, description=description).first()
        if user:
            if description is None and data is not None:
                user.data = data
                db.session.commit()
            elif description is not None and data is None:
                user.description = description
                db.session.commit()
            elif description is not None and data is not None:
                user.description = description
                user.data = data
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

    def delete_report(self, reportname, description, data):
        print(reportname, description, data)
        user = TestReport.query.filter_by(reportname=reportname).first()
        print(user)
        if user:
            db.session.delete(user)
            db.session.commit()
            return {
                'errcode': 0,
                'errmsg': f'{reportname}已删除'
            }
        else:
            return {
                'errcode': 1,
                'errmsg': f'{reportname}不存在'
            }
