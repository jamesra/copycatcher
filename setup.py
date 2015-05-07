'''
Created on Aug 30, 2013

@author: James Anderson
'''

import glob
import os


from ez_setup import use_setuptools


# This if test prevents an infinite recursion running tests from "python setup.py test"
if __name__ == '__main__':

    use_setuptools()
    
    from setuptools import setup, find_packages
    
    packages = find_packages()
    
    install_requires = ["pdf2text"]

    provides = ["copy_catcher"]
    
    classifiers = ['Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 2.7']

    dependency_links = ["git+http://github.com/jamesra/copycatcher#egg=copy_catcher-1.0.0"]

    package_dir = {'copy_catcher' : 'copy_catcher'}

    scripts = glob.glob(os.path.join('scripts', 'main.py'))

    entry_points = {'console_scripts': ['copycatcher = copy_catcher.main:Execute']}
    
    setup(name='copy_catcher',
          zip_safe=True,
          version='1.0.0',
          scripts=scripts,
          classifiers=classifiers,
          description="Find matching text blocks in files",
          author="James Anderson",
          author_email="James.R.Anderson@utah.edu",
          url="http://jamesra.github.com/copy_catcher",
          packages=packages,
          entry_points=entry_points,
          install_requires=install_requires,
          provides=provides,
          test_suite="test",
          dependency_links=dependency_links)
