from setuptools import setup, find_packages

version = '0.1'
description = 'Python modules of the book Introduction to Programming in Python by Robert Sedgewick, Kevin Wayne and Robert Dondero. Original code available at https://introcs.cs.princeton.edu/python/code/'

setup(
    name='introcs',
    version=version,
    description=description,
    install_requires=['pygame'],
    packages=find_packages(),
    package_dir=['.'] 
)