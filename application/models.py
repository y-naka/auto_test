#!/usr/bin/env python
# vim:fileencoding=utf-8
# Author: Shinya Suzuki
# Created: 2017-11-16

from application import db
from application import app


class Profile(db.Model):
    __tablename__ = "profiles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    role = db.Column(db.Text)

    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role

    def __repr__(self):
        return "<Profile {0}>".format(self.name)


class Message(db.Model):
    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text)

    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return "<Message {0}>".format(self.message)


@app.before_first_request
def init_schema():
    db.create_all()


def init_data(initialized_data=None):
    if initialized_data is None:
        initialized_data = {}
    for k in initialized_data.keys():
        data = initialized_data[k]
        for d in data:
            if k == "profile":
                q = Profile(name=d["name"], email=d["email"], role=d["role"])
            elif k == "message":
                q = Message(message=d["message"])
            else:
                raise ValueError("Invalid key for schema: {0}".format(k))
            db.session.add(q)
    db.session.commit()


def drop():
    db.drop_all()
