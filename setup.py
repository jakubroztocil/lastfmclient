import codecs
from setuptools import setup

import lastfmclient


setup(
    name='lastfmclient',
    version=lastfmclient.__version__,
    description=lastfmclient.__doc__.strip(),
    long_description=codecs.open('README.rst', encoding='utf8').read(),
    author_email=lastfmclient.__email__,
    license=lastfmclient.__licence__,
    url='https://github.com/jakubroztocil/lastfmclient',
    download_url='https://github.com/jakubroztocil/lastfmclient',
    packages=['lastfmclient'],
    install_requires=[
        'requests>=1.0.4'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
