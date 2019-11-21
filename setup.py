#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'beautifulsoup4',
    'nltk',
    'numpy',
    'pandas',
    'scrapy',
    'Click', ]

setup_requirements = [
    'bump2version',
    'pytest-runner',
    'twine',
    'wheel',
    'Sphinx', ]

test_requirements = [
    'coverage',
    'flake8',
    'pytest',
    'tox',
    'watchdog', ]

setup(
    author="David Mougeolle",
    author_email='moodule@protonmail.com',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Find the most relevant ads on the whole web! :dart:",
    entry_points={
        'console_scripts': [
            'homespace=homespace.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='homespace',
    name='homespace',
    packages=find_packages(include=['homespace', 'homespace.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/moodule/homespace',
    version='0.1.0',
    zip_safe=False,
)
