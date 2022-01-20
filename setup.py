from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'The predecessor to cognitare from the book NNFS'

# Setting up
setup(
    name="tensorking",
    version=VERSION,
    author="dandisk (David King)",
    author_email="<dandisk@protonmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['numpy'],

)