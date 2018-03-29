"""
PySoundIo

A robust, cross-platform solution for real-time audio.
"""
import re
from setuptools import setup, Extension

vstr = open('pysoundio/__init__.py', 'r').read()
regex = r"^__version__ = ['\"]([^'\"]*)['\"]"
version = re.search(regex, vstr, re.M)

soundio = Extension('_soundiox',
                    sources=['pysoundio/_soundiox.c'],
                    libraries=['soundio'])

setup(
    name='pysoundio',
    version=version.group(1),
    description='Python wrapper for libsoundio',
    long_description='A robust, cross-platform solution for real-time audio',
    license='MIT',
    author='Joe Todd',
    author_email='joextodd@gmail.com',
    url='https://github.com/joextodd/pysoundio',
    download_url = 'https://github.com/joextodd/pysoundio/archive/' + version.group(1) + '.tar.gz',
    packages=['pysoundio', 'examples', 'tests'],
    ext_modules=[soundio],
    test_suite='tests',
    keywords=('audio', 'sound', 'stream')
)