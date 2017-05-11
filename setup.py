#!/usr/bin/env python
from setuptools import setup

# version_tuple = __import__('xadmin').VERSION
# version = ".".join([str(v) for v in version_tuple])

setup(
    name='XadminSelect2',
    version='0.6.1',
    author='wgb237',
    author_email='wgb237@gmail.com',
    url='https://github.com/wgbbiao/xadmin-select2',
    download_url='https://github.com/wgbbiao/xadmin-select2/archive/master.zip',
    packages=['XadminSelect2'],
    package_data = {
        'XadminSelect2': ['*.js'],
    },
    include_package_data=True,
    install_requires=[
        'xadmin',
    ],
    zip_safe=False,
    keywords=['bootstrap'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        "Programming Language :: JavaScript",
        'Programming Language :: Python',
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)