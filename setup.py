#!/usr/bin/env python

from setuptools import setup, find_packages

import os
import sys

version = os.getenv("VERSION")
if not version:
    print("no version supplied")
    sys.exit(1)

setup(
    name="polygon-api-client",
    version=version,
    description="Polygon API client",
    author_email="ricky@polygon.io",
    url="https://github.com/Polygon-io/client-python",
    packages=find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
