from peewee import SqliteDatabase
from pyramid.request import Request


# TODO prepare logic this way that we can use database url in ini settings
db = SqliteDatabase('pyramid_hs.db')


class MyRequest(Request):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        db.get_conn()
        self.add_finished_callback(self.finish)

    def finish(self, request):
        if not db.is_closed():
            db.close()