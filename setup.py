# -*- coding: utf-8 -*-
import re
from setuptools import setup, find_packages


INSTALL_REQUIRES = ("marshmallow>=2.15.2",)
EXTRAS_REQUIRE = {
    "lint": [
        "flake8==3.8.1",
        'flake8-bugbear==19.8.0; python_version >= "3.5"',
        "pre-commit~=1.18",
    ],
    "tests": ["pytest", "mock", "webargs>=0.11.0", "WTForms>=2.0.1", "colander>=1.0"],
}
EXTRAS_REQUIRE["dev"] = EXTRAS_REQUIRE["tests"] + EXTRAS_REQUIRE["lint"] + ["tox"]


def find_version(fname):
    """Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    """
    version = ""
    with open(fname, "r") as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError("Cannot find version information")
    return version


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content


setup(
    name="marshmallow-validators",
    version=find_version("marshmallow_validators/__init__.py"),
    description="Use 3rd-party validators (e.g. from WTForms and colander) with marshmallow",
    long_description=read("README.rst"),
    author="Steven Loria",
    author_email="sloria1@gmail.com",
    url="https://github.com/marshmallow-code/marshmallow-validators",
    packages=find_packages(exclude=("test*",)),
    package_dir={"marshmallow-validators": "marshmallow-validators"},
    include_package_data=True,
    extras_require=EXTRAS_REQUIRE,
    install_requires=INSTALL_REQUIRES,
    license="MIT",
    zip_safe=False,
    keywords="validators marshmallow",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    test_suite="tests",
    project_urls={
        "Bug Reports": "https://github.com/marshmallow-code/marshmallow-validators/issues",
        "Funding": "https://opencollective.com/marshmallow",
    },
)
