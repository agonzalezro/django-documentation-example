django-documentation-example
============================

This is just an example of how to write documentation in django projects.

Setup
-----

    $ mkvirtualenv [whatever]
    $ pip install -r requirements.txt

Creating docs configuration
---------------------------

*I've removed the explanations of the questions, just run the command if you
wanna see them.*

You don't need to follow this steps in this projects since the configuration
is already created, but I wrote it here FYI.

    $ sphinx-quickstart

    > Root path for the documentation [.]: docs
    > Separate source and build directories (y/N) [n]:
    > Name prefix for templates and static dir [_]:
    > Project name: Just an example
    > Author name(s): Álex González
    > Project version: 0.1
    > Project release [0.1]:
    > Source file suffix [.rst]:
    > Name of your master document (without suffix) [index]:
    > Do you want to use the epub builder (y/N) [n]:
    > autodoc: automatically insert docstrings from modules (y/N) [n]: y
    > doctest: automatically test code snippets in doctest blocks (y/N) [n]: y
    > intersphinx: link between Sphinx documentation of different projects (y/N) [n]: y
    > todo: write "todo" entries that can be shown or hidden on build (y/N) [n]:
    > coverage: checks for documentation coverage (y/N) [n]:
    > pngmath: include math, rendered as PNG images (y/N) [n]:
    > mathjax: include math, rendered in the browser by MathJax (y/N) [n]:
    > ifconfig: conditional inclusion of content based on config values (y/N) [n]:
    > viewcode: include links to the source code of documented Python objects (y/N) [n]: y
    > Create Makefile? (Y/n) [y]:
    > Create Windows command file? (Y/n) [y]: n

The only changes that we need to do after this wizard is edit the generated
`conf.py` file and:

- add our `syspath` there (there is a commented line).

- add the `sphinx.ext.graphviz` extensions to the list of installed extensions.

Write your documentation
------------------------

I will not add this to the `README.md` but if you check the source code of the
app you can see how I wrote some example documentation for you to follow. But,
please, take a look to the
[sphinx tutorial](http://sphinx-doc.org/latest/tutorial.html).
That link is invaluable.

Generating docs
---------------

    $ cd docs
    $ make html

Where is my documentation
-------------------------

You will find it on `./docs/_build/html/index.html`.

I ignored the `_build` path to force you to create the documentation by hand :)
