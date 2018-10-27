#!/usr/bin/env python

from setuptools import setup

# Installation dependencies
install_requires = [
   'django>=1.11,<1.12',
   'wagtail>=2.3,<2.4',
]

setup(
    name='wagtail-pythonanywhere-quickstart',
    version='1.0.1',
    license='ISC License (ISCL)',
    description='Wagtail CMS quickstart for deployment on PythonAnywhere',
    long_description=open('README.rst').read(),
    url='https://github.com/texperience/wagtail-pythonanywhere-quickstart',
    author='Timo Rieber',
    author_email='trieber@texperience.de',
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Wagtail :: 1',
        'Framework :: Wagtail :: 2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
