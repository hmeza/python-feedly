#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='feedlyclient',
    version='0.0.1',
    url='',
    license='',
    packages=find_packages(),
    author='zgw21cn',
    author_email='',
    description='Client for Feedly ',
    include_package_data=True,
    install_requires=[
        'requests',
    ],
)
