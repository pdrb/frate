from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


version = '0.3'


setup(
    name='frate',
    version=version,
    description='Show file growing rate in real time',
    long_description=long_description,
    author='Pedro Buteri Gonring',
    author_email='pedro@bigode.net',
    url='https://github.com/pdrb/frate',
    license='MIT',
    classifiers=[],
    keywords='file rate growing line lines filerate frate',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    entry_points={
        'console_scripts': ['frate=frate.frate:cli'],
    },
)
