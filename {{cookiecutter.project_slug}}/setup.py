import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding="utf-8") as fd:
        return re.sub(text_type(r":[a-z]+:`~?(.*?)`"), text_type(r"``\1``"), fd.read())


requirements = [
]


setup(
    name="{{ cookiecutter.package_name }}",
    version="{{ cookiecutter.version }}",
    url="{{ cookiecutter.package_url }}",
    author="{{ cookiecutter.author_full_name }}",
    author_email="{{ cookiecutter.author_email }}",
    description="{{ cookiecutter.project_short_description }}",
    long_description=read("README.md"),
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=("tests",)),
    install_requires=requirements,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6"
    ],
)
