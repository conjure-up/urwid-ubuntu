# Copyright 2015 Canonical, Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
urwid-ubuntu
============

Ubuntu styled widgets for urwid.
"""

from setuptools import setup, find_packages

setup(name='ubuntui',
      version="0.0.1",
      description="Urwid widgets used in Ubuntu console apps",
      long_description=__doc__,
      author="Canonical Solutions Engineering",
      author_email='ubuntu-dev@lists.ubuntu.com',
      url="https://github.com/Ubuntu-Solutions-Engineering/urwid-ubuntu",
      license="AGPLv3+",
      packages=find_packages(exclude=['test']))
