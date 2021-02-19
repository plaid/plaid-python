from setuptools import setup, find_packages

VERSION='8.0.0b9'
url = 'https://github.com/plaid/plaid-python'

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
  "nulltype",
]

setup(
    name='plaid-python',
    version=VERSION,
    description='Python client library for the Plaid API and Link',
    long_description='',
    keywords='api, client, plaid',
    author='Plaid Technologies',
    author_email='developers@plaid.com',
    url=url,
    download_url='{}/tarball/v{}'.format(url, VERSION),
    license='MIT',
    packages=find_packages(exclude='tests'),
    package_data={'README': ['README.md']},
    python_requires=">=3.6",
    install_requires=REQUIRES,
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: Web Environment",
    ]
)