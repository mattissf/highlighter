#!/usr/bin/env python

from distutils.core import setup

setup(
    name='Highlighter',
    version='1.0',
    description='Highlights words in a stream',
    author='Mattis Stordalen Flister',
    author_email='mattis.stordalen.flister@gmail.com',
    py_modules=['highlighter'],
    scripts=['bin/hl'],
 )
