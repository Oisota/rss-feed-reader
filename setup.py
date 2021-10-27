import pathlib

from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='feed-reader',
    version='0.1.0',
    description='RSS/Atom Feed Reader',
    long_description=long_description,
    packages=find_packages(),
)