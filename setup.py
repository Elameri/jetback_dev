from setuptools import setup, find_packages
import os

def read_requirements(file):
    return [line.strip() for line in open(file) if line.strip() and not line.startswith('#')]

setup(
    name="jetback_dev",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=read_requirements('requirements/base.txt'),
    extras_require={
        'flask': read_requirements('requirements/flask.txt'),
        'fastapi': read_requirements('requirements/fastapi.txt'),
        'django': read_requirements('requirements/django.txt'),
    },
)