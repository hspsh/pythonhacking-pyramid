import datetime

from peewee import Model, CharField, IntegerField, DateField, BooleanField, ForeignKeyField

from pyramid_hs.db import db


class BaseModel(Model):
    created = DateField(default=datetime.datetime.now)

    class Meta:
        database = db

class MyModel(BaseModel):
    name = CharField()
    value = IntegerField()


class Person(BaseModel):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()


class Pet(BaseModel):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()