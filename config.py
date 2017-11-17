#!/usr/bin/env python
# vim:fileencoding=utf-8
# Author: Shinya Suzuki
# Created: 2017-11-16

database_path = "/techathon.db"
SQLALCHEMY_DATABASE_URI = "sqlite://{0}".format(database_path)
SECRET_KEY = 'takuji@bio.titech.ac.jp'
SQLALCHEMY_TRACK_MODIFICATIONS = True
