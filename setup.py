import re
from setuptools import setup, find_packages

with open('plaid/version.py', 'r') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

url = 'https://github.com/plaid/plaid-python'

setup(
    name='plaid-python',
    version=version,
    description='Python client library for the Plaid API and Link',
    long_description='',
    keywords='api, client, plaid',
    author='Plaid Technologies',
    author_email='developers@plaid.com',
    url=url,
    download_url='{}/tarball/v{}'.format(url, version),
    license='MIT',
    packages=find_packages(exclude='tests'),
    package_data={'README': ['README.md']},
    install_requires=['requests>=2.7.0'],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: Web Environment",
    ]
)
