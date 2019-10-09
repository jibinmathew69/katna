#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import setuptools
from distutils.core import Command

with open("README.md", "r") as fh:
    long_description = fh.read()

# helper functions to make it easier to list dependencies not as a python list, but vertically w/ optional built-in comments to why a certain version of the dependency is listed
def cleanup(x):
    return re.sub(r" *#.*", "", x.strip())  # comments


def to_list(buffer):
    return list(filter(None, map(cleanup, buffer.splitlines())))


# normal dependencies ###
#
# these get resolved and installed via either of these two:
#
#   pip install katna
#   pip install -e .
#
# IMPORTANT: when updating these, please make sure to sync conda/meta.yaml
dep_groups = {
    "core": to_list(
        """
        scipy
        scikit-learn
        scikit-image
        opencv-contrib-python>=3.4.7
        numpy>=1.15
        imutils
        requests
"""
    )
}

requirements = [y for x in dep_groups.values() for y in x]
setup_requirements = to_list(
    """
    pytest-runner
    setuptools>=36.2
"""
)


# test dependencies ###
test_requirements = to_list(
    """
    pytest
"""
)


setuptools.setup(
    name="katna",
    version="0.3.0.0",
    author="keplerlab",
    author_email="keplerwaasi@gmail.com",
    description="Katna is a tool that automates video key/best frames extraction.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/keplerlab/Katna.git",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    setup_requires=setup_requirements,
    tests_require=test_requirements,
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Documentation": "https://keplervaani.com/katna",
        "Source": "https://github.com/keplerlab/Katna",
        "Tracker": "https://github.com/keplerlab/Katna/issues",
    },
    include_package_data=True,
    zip_safe=False,
)