"""Surveyor is an applicaiton and not a library.  To correctly install it, follow steps in the
Dockerfile or docker-compose.yaml.  Direct installation through pip doesn't do anything."""

from setuptools import setup

setup(
    name='Surveyor',
    version='0.1.0',
    description='A user survey tool',
    author='Ramsey Barghouti',
    author_email='ramsey.barghouti@gmail.com',
)
