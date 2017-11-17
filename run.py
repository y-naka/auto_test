#!/usr/bin/env python
# vim:fileencoding=utf-8
# Author: Shinya Suzuki
# Created: 2017-11-16

from application import app
from application.models import init_schema, init_data
import click


@app.cli.command(help="Initialize database")
def initdb():
    init_schema()
    init_data({"profile": [{"name": "Takuji Yamada", "email": "takuji.yamada@example.co.jp", "role": "CTO"}]})
    click.echo("Database is initialized.")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True, debug=True)
