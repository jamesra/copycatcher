.. CopyCatcher Documentation master file.

######################################
Welcome to CopyCatcher's Documentation
######################################

.. toctree::
   :maxdepth: 1 
   
About
-----

Copy Catcher was created to find suspiciously similiar blocks of text in student assignments.

Why Copy catcher
----------------

There are a number of programs on the internet to detect plagarism.  However 
most are concerned about internet sources.  Copy Catcher focuses on cheating
within the class.  CopyCatcher was originally written to find duplicated portions of
patient care plans in a medical education course.

How it works
------------

Each Word or PDF file in a chosen directory is converted to a text file.  For every word in the text file we build a set from the nearest N adjacent words.
This set of words is sorted to create a dictionary key.  We then create or append a list with the filename for that dictionary key.  After all files are 
processed we check for keys present in multiple files and present a report suggesting which files warrant investigation.

Installation
------------

First make sure you have a `git client`_ installed.
CopyCatcher is a Python program, so ensure you have `Python`_ installed as well.

Once python is installed go to a command console.  Go to the python scripts directory and install copycatcher with Pip. 
Better directions can be found on Google if these are overly brief.::

   pip install git+https://jamesra.github.io/copycatcher#master
   
Use
---

A good start is to ensure each file is named after the student so the results can be easily interpreted.

Some assignments have duplicate text included.  For example questions shared across all assignments.  Specify the name of a file in the folder which contains text which should be excluded from the duplicate results.

.. argparse::
   :module: copy_catcher.main
   :func: CreateParser
   :prog: copycatcher  
   
Example
-------

Find all of the duplicates in the C:\Docs directory using a blocksize of 7 and excluding blocks found in a questions.doc file

::

    copycatcher C:\Docs -blocksize 6 -template questions.doc
   


.. _git client:  http://git-scm.com/download
.. _Python: http://python.org

