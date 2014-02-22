from ez_setup import use_setuptools

use_setuptools()

from setuptools import setup, find_packages


setup(
    name='python-plaid',
    version='0.1.0',
    description='Simple Python API client for Plaid',
    long_description='',
    keywords='api, client, plaid',
    author='Chris Forrette',
    author_email='chris@chrisforrette.com',
    url='https://github.com/chrisforrette/python-plaid',
    license='MIT',
    packages=find_packages(exclude='tests'),
    package_data={'README': ['README.md']},
    install_requires=['requests==2.2.1'],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: Web Environment",
    ]
)
