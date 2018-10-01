# coding: utf-8

"""
    Blackfynn Swagger

    Swagger documentation for the Blackfynn api  # noqa: E501

    OpenAPI spec version: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "datcore-sdk"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]
REQUIRES.append("aiohttp")

setup(
    name=NAME,
    version=VERSION,
    description="Blackfynn Swagger",
    author_email="",
    url="https://github.com/mguidon/aiohttp-dsm/tree/master/datcore-sdk/python",
    keywords=["OpenAPI", "OpenAPI-Generator", "Blackfynn Swagger"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Swagger documentation for the Blackfynn api  # noqa: E501
    """
)
