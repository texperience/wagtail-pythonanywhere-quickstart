#!/usr/bin/env python

from setuptools import setup

# Installation dependencies
install_requires = [
   'django>= 1.11,<1.12',
   'wagtail>=1.12,<1.13',
]

setup(
    name='wagtail-pythonanywhere-quickstart',
    version='1.0.0',
    license='ISC License (ISCL)',
    description='Wagtail CMS quickstart for deployment on PythonAnywhere',
    long_description=open('README.rst').read(),
    url='https://github.com/texperience',
    author='Timo Rieber',
    author_email='trieber@texperience.de',
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 4 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
