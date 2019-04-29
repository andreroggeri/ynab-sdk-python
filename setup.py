from setuptools import setup, find_packages

NAME = 'ynab-sdk'
VERSION = '1.0.0'
REQUIRES = ['requests']

setup(
    name=NAME,
    version=VERSION,
    description="YNAB API Endpoints",
    author_email="",
    url="",
    keywords=["Swagger", "YNAB API Endpoints"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.youneedabudget.com  # noqa: E501
    """
)
