#!/usr/bin/env python
# vim:fileencoding=utf-8
# Author: Shinya Suzuki
# Created: 2017-11-16

from flask import render_template, request
from application import app, db
from application.models import Profile
from application.models import Message


@app.route('/')
def route_index():
    return render_template('index.html')


@app.route('/profile')
def route_profile():
    id = request.args.get('id', type=int)
    if id is not None:
        profiles = Profile.query.get(id)
        if profiles is not None:
            return render_template('profile.html', profile=profiles)
        else:
            return render_template('profile.html')
    else:
        return render_template('profile.html')


@app.route('/bbs', methods=['GET', 'POST'])
def route_bbs():
    if request.method == 'POST':
        m = request.form['message']
        message = Message(
            message=m
        )
        db.session.add(message)
        db.session.commit()
    messages = Message.query.with_entities(Message.message)
    return render_template('bbs.html', messages=messages)
