#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='blanc-basic-pages',
    version='0.3.2',
    description='Blanc Basic Pages for Django',
    long_description=open('README.rst').read(),
    url='https://github.com/blancltd/blanc-basic-pages',
    maintainer='Alex Tomkins',
    maintainer_email='alex@blanc.ltd.uk',
    platforms=['any'],
    install_requires=[
        'django-mptt>=0.6.1',
        'django-mptt-admin>=0.1.8',
    ],
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
    license='BSD',
)
