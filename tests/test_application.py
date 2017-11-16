#!/usr/bin/env python
# vim:fileencoding=utf-8
# Author: Shinya Suzuki
# Created: 2017-11-16

import unittest
from application import app


class TestApplication(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
