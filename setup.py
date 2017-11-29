"""
urwid-ubuntu
============

Ubuntu styled widgets for urwid.
"""

from setuptools import setup, find_packages

setup(name='ubuntui',
      version="0.1.8",
      description="Urwid widgets used in Ubuntu console apps",
      long_description=__doc__,
      author="Canonical Solutions Engineering",
      author_email='ubuntu-dev@lists.ubuntu.com',
      url="https://github.com/canonicalltd/urwid-ubuntu",
      license="LGPL-3.0",
      packages=find_packages(exclude=['test']),
      install_requires=['urwid'])
