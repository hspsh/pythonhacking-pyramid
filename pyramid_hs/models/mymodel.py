import datetime

from peewee import Model, CharField, DateField

from pyramid_hs.db import db


class BaseModel(Model):
    created_at = DateField(default=datetime.datetime.now)

    class Meta:
        database = db


class Todo(BaseModel):
    title = CharField(max_length=200)
    desc = CharField(null=True, default=None)
