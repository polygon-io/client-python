#!/usr/bin/env python

from setuptools import setup, find_packages

import os
import sys

version = os.getenv("VERSION")
if not version:
    print("no version supplied")
    sys.exit(1)

def get_readme_md_contents():
    """read the contents of your README file"""
    with open("README.md", encoding='utf-8') as f:
        long_description = f.read()
        return long_description

setup(
    name="polygon-api-client",
    version=version,
    description="Polygon API client",
    long_description=get_readme_md_contents(),
    long_description_content_type="text/markdown",
    author_email="support@polygon.io",
    url="https://github.com/polygon-io/client-python",
    packages=find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Office/Business :: Financial :: Investment"
    ],
    install_requires=[
        "websocket-client==0.56.0",
        "websockets==8.0.2",
        "requests==2.22.0"
    ]
)
