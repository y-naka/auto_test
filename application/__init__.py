#!/usr/bin/env python
# vim:fileencoding=utf-8
# Author: Shinya Suzuki
# Created: 2017-11-16

from logging import getLogger, DEBUG, Formatter, StreamHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def get_logger():
    logger = getLogger(__name__)
    logger.setLevel(DEBUG)
    log_fmt = '%(asctime)s : %(name)s : %(levelname)s : %(message)s'
    formatter = Formatter(log_fmt)
    stream_handler = StreamHandler()
    stream_handler.setLevel(DEBUG)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


app = Flask(__name__)
app.config.from_object("config")

db = SQLAlchemy(app)
import application.views
