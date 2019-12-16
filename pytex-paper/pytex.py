#!/usr/bin/env python
# -*- coding: utf-8 -*-

r"""
PyTeX is a simple way of paper writing using LaTeX.
You can write your papers in a python script and make it ready to be compiled in various compilers of LaTeX.
PyTeX  
======
You can write sections, subsections, subsubsections,
and other additional items and tags in your ordinary content files.
(this property needs a base knowledge about LaTeX)

Usage
-------

   >>>  article = pytex.document() # Create a document object | You can also set paper options here
   >>>  article.content('Introduction to PyTeX', # Topic title
   ...                            'Paul Jeff', # Name of author
   ...                            'paul.jeff@gmail.com +123456789', # Contact details
   ...                            'my_abs.txt', # Abstraction file
   ...                            {
   ...                              'Introduction':'intro.txt', # {'Section name':'Content File'}
   ...                              'Start with Numpy':'start.txt',
   ...                              'Installation':'install.txt'
   ...                            })
   >>>  article.release() # Release tex file
   >>>  article.compile() # Compile tex file

Methods & Parameters
--------------------------

`document.content` includes a bunch of parameters. It has some default values.
`document.compile` makes your file ready to be compiled.

`document.__init__` sets vital vars of your paper properties which is `option` in LaTeX.
`document.release` writes the tex file.

PyTeX has been released from PyPi and licensed by `GPL-3`

Repo ~> <https://github.com/lnxpy/pytex>
------------------------------
Document ~> <https://github.com/lnxpy/pytex/*************>
------------------------------
Website ~> <http://lnxpy.unaux.com>
------------------------------

Made with 💙 on 2019 by Alireza Yahyapour
"""

from os import system as sys
# using platform.system to get the OS
from platform import system

__all__ = [
    '__init__',
    'release',
    'content',
    'compile'
]
__author__ = [
    'Alireza Yahyapour',
    'http://lnxpy.unaux.com',
    'https://github.com/lnxpy'
]
__publish__ = [
    'Sep 2019'
]
__license__= [
    'https://######'
]

class LaTeX:
    def __init__(self, size='11pt', paper='a4paper', column='onecolumn', side='oneside'):
        self.size = size
        self.paper = paper
        self. column = column
        self.side = side
        self.type = type
    def release(self, content={}):
        content.clear()
        # create content var to explain properties like LaTeX syntax
        content = {
            'option': ', '.join([self.size,self.paper,self.column,self.side]),
            'class': self.type,
            'content': {'title':self.title,'author':self.author,'abstract':open(self.abstraction,'r').read(),'substance':self.substance}}
        for i in content['content']['substance'].keys():
            data = open(content['content']['substance'][i],'r').read()
            content['content']['substance'][i] = data
        try:
            lastrel = open(content['content']['title']+'.tex','w')
        except Exception as identifier:
            lastrel = open(content['content']['author']+'.tex','w')
        const = {
            '^option^':content['option'],
            '^class^':content['class'],
            '^title^':content['content']['title'],
            '^author^':content['content']['author']
        }
        # rewrite using temp.tex
        with open('temp.tex','r') as tempfile:
            for line in tempfile.readlines():
                for element in const:
                    if element in line:
                        line = line.replace(element,const[element])
                lastrel.write(line)
            lastrel.write('\n')
        lastrel.write(content['content']['abstract']+'\n')
        lastrel.write('\\end{abstract}'+'\n')
        for i in content['content']['substance'].keys():
            lastrel.write('\\%s{%s}{\n'%('section',i))
            lastrel.write(content['content']['substance'][i])
            lastrel.write('\n}\n')
        lastrel.write('\\end{document}')

class document(LaTeX):
    def content(self, title, author, email, abstraction, substance = {}):
        self.type = 'article'
        self.title = title
        self.author = '%s\t\\texttt{%s}'%(author, email)
        self.abstraction = abstraction
        self.substance = substance
    # compile operation
    def compile(self):
        if system() == 'Windows':
            pass
        elif system() == 'Linux':
            pass
