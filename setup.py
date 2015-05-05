'''
Created on Aug 30, 2013

@author: James Anderson
'''

import glob
import os

from setuptools import setup, find_packages

from ez_setup import use_setuptools


# This if test prevents an infinite recursion running tests from "python setup.py test"
if __name__ == '__main__':

    use_setuptools()

    install_requires = ["pdf2text"]

    packages = find_packages()

    provides = ["copy_catcher"]

    dependency_links = []

    package_dir = {'copy_catcher' : 'copy_catcher'}

    scripts = glob.glob(os.path.join('scripts', 'main.py'))

    entry_points = {'console_scripts': ['copycatcher = copy_catcher.main:Execute']}

    setup(name='copy_catcher',
          zip_safe=True,
          version='1.0.0',
          scripts=scripts,
          description="Find similiar text in files",
          author="James Anderson",
          author_email="James.R.Anderson@utah.edu",
          url="https://jamesra.github.com/copy_catcher",
          packages=packages,
          entry_points=entry_points,
          install_requires=install_requires,
          provides=provides,
          test_suite="test",
          dependency_links=dependency_links)
