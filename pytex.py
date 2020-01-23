#!/usr/bin/env python
# -*- coding: utf-8 -*-

r"""
PyTeX is a simple way of paper writing using LaTeX with low knowledge of LaTeXing.
You can write your papers in the python script and make them ready to be compiled in the various compilers of LaTeX.
PyTeX  
======
You can write sections, subsections, subsubsections,
and other additional items and tags in your ordinary content files. (this property needs a base knowledge about LaTeX)

Usage
-------

   >>>  article = pytex.document()
   >>>  article.content('Introduction to PyTeX',
   ...                            'Paul Jeff',
   ...                            'paul.jeff@gmail.com +123456789',
   ...                            'my_abs.txt',
   ...                            {
   ...                              'Introduction':'intro.txt',
   ...                              'Start with Numpy':'start.txt',
   ...                              'Installation':'install.txt'
   ...                            })
   >>>  article.release()

Methods & Parameters
--------------------------

`document.content` includes a bunch of parameters. It has some default values.

`document.__init__` sets vital vars of your paper properties which is `option` in LaTeX.
`document.release` executes the tex file.

PyTeX has been released from PyPi and licensed by `MIT on 2020`.
Made with love on 2019 and maintaned on 2020 by Ali Reza Yahyapour(lnxpy).
"""

__all__ = [
    '__init__',
    'release',
    'content',
]
__author__ = [
    'Ali Reza Yahyapour',
    'http://lnxpy.unaux.com',
    'https://github.com/lnxpy',
]
__publish__ = [
    'Sep 2019',
]
__license__= [
    'MIT License Copyright (c) 2019 Ali Reza Yahyapour',
    'https://github.com/lnxpy/PyTeX/blob/master/LICENSE.txt',
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
        template = [
            '\documentclass[^option^]{^class^}',
            '\begin{document}',
            '\title{^title^}\maketitle',
            '\author{\centering{\textbf{^author^}\par}}',
            '\begin{abstract}']
        for line in template:
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
