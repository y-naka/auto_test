#!/usr/bin/env python
# vim:fileencoding=utf-8
# Author: Shinya Suzuki
# Created: 2017-11-16

import os
import tempfile
import unittest
import json
from application import app
from application.models import Profile, Message, drop, init_schema, init_data


class TestApplicationModel(unittest.TestCase):

    def setUp(self):
        self.db_fd, app.config["database_path"] = tempfile.mkstemp()
        app.config["TESTING"] = True
        self.app = app.test_client()
        d_dir = os.path.dirname(__file__) + "/data/test_application"
        init_json = os.path.join(d_dir, "init.json")
        with open(init_json, "r") as f:
            initialized_data = json.load(f)
        init_schema()
        init_data(initialized_data)

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config["database_path"])
        drop()

    def test_profile(self):
        yamada = Profile.query.get(4)
        self.assertEqual(yamada.id, 4)
        self.assertEqual(yamada.name, "Takuji Yamada")
        self.assertEqual(yamada.email, "takuji.yamada@example.com")
        self.assertEqual(yamada.role, "Associate professor")
        yamada = Profile.query.get(5)

    def test_profile_repr(self):
        yamada = Profile.query.get(4)
        self.assertEqual(yamada.__repr__(), "<Profile Takuji Yamada>")

    def test_message(self):
        messages = Message.query.all()
        self.assertEqual(len(messages), 1)

    def test_profile_empty(self):
        input1 = 5
        result1 = Profile.query.get(input1)
        self.assertEqual(None, result1)


if __name__ == "__main__":
    unittest.main()
