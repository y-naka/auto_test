#!/usr/bin/env python
# vim:fileencoding=utf-8
# Author: Shinya Suzuki
# Created: 2017-11-16

try:
    from setuptools import setup, find_packages
except ImportError:
    raise ImportError("Please install setuptools.")

setup(
    name="sample_application",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask",
        "Flask-SQLAlchemy"
    ],
    setup_requires=[
        "pytest-runner"
    ],
    tests_require=[
        "pytest"
    ],
    license="BSD 3-Clause License",
    url="http://tsubaki.bio.titech.ac.jp/NY-lab/techathon/sample_application",
    author="Shinya SUZUKI",
    author_email="sshinya@bio.titech.ac.jp",
    description="Sample application by Flask"
)
