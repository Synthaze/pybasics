#!/usr/bin/env python3
from setuptools import setup
import os


with open(os.path.dirname(os.path.realpath(__file__)) + '/requirements.txt') as f:
    required = f.read().splitlines()

setup(install_requires=required)
