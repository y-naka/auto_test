#!/usr/bin/env python
# vim:fileencoding=utf-8
# Author: Shinya Suzuki
# Created: 2017-11-16

import os
import tempfile
import unittest
import json
from application import app
from application.models import Message, drop, init_schema, init_data


class TestApplication(unittest.TestCase):

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

    def test_get_root(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)

    def test_post_bbs(self):
        input1 = "Test message"
        self.app.post("/bbs", data={
            "message": input1
        })
        messages = [m.message for m in Message.query.all()]
        self.assertIn(input1, messages)

    def test_get_bbs(self):
        response = self.app.get("/bbs")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
