from db.database import db, AssertStatus


class SevenirubyAssertStatus:
    def get_status(self):
        r = []
        for t in AssertStatus.query.all():
            res = {}
            res['id'] = t.id
            res['errmsg'] = t.errmsg
            res['errcode'] = t.errcode
            r.append(res)
        return r