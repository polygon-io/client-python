#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="polygon",
    version="0.0.1",
    description="Polygon API client",
    author_email="ricky@polygon.io",
    url="",
    keywords=["Polygon API"],
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=["polygon"],
    include_package_data=True
)
