from setuptools import setup, find_packages
import plaid


url = 'https://github.com/plaid/plaid-python'

setup(
    name='plaid-python',
    version=plaid.__version__,
    description='Simple Python API client for Plaid',
    long_description='',
    keywords='api, client, plaid',
    author='Chris Forrette',
    author_email='chris@chrisforrette.com',
    url=url,
    download_url='{}/tarball/v{}'.format(url, plaid.__version__),
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
