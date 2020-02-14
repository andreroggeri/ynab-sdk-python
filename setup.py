import os

from setuptools import setup, find_packages

NAME = 'ynab-sdk'
VERSION = '0.0.4'
REQUIRES = ['requests', 'python-dateutil', 'redis']


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


setup(
    name=NAME,
    version=VERSION,
    description='YNAB API Endpoints',
    author_email='a.roggeri.c@gmail.com',
    url='https://github.com/andreroggeri/ynab-sdk-python',
    keywords=["YNAB", "YNAB API Endpoints", ''],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description=read('README.md'),
    long_description_content_type='text/markdown'
)
