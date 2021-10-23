import sys

from rich import traceback
traceback.install()


sys.path.insert(0, "")

# -- Project information -----------------------------------------------------

project = 'Github-blaisep'
# year = datetime.now().year
# copyright = f"{year}, Blaise Pabon"
author = 'Blaise Pabon'

# The full version, including alpha/beta/rc tags
release = '0.0.9'

# -- General configuration ---------------------------------------------------
extensions = ['sphinx.ext.autodoc', # creates docs from the compiler output and docstrings
              'sphinx.ext.doctest', # tests the code in examples to make sure they work
              'sphinx.ext.autosummary', #
              'sphinx.ext.napoleon', # https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html)
              # 'sphinx.ext.intersphinx', # Extends search queries to other sites, like python.org
              # 'sphinx.ext.todo', # Finds items marked to do and puts them in the docs.
              # 'sphinx.ext.coverage', # checks code coverage
              # 'sphinx.ext.mathjax', # represents math expressions in Javascript
              # 'sphinx.ext.ifconfig', # conditional execution based on flags
               'sphinx.ext.viewcode', # enables the "view page's source code" option in the HTML.
              # 'sphinx_rtd_theme', # layouts and structures used on ReadTheDocs
              # 'sphinxcontrib.openapi', # https://sphinxcontrib-openapi.readthedocs.io/#)
              # 'sphinxcontrib.redoc' , # https://sphinxcontrib-redoc.readthedocs.io/en/stable/)
              'sphinx.ext.githubpages', # prepares HTML for hosting on Github
              'sphinx_copybutton', # pip install sphinx-copybutton (note the hyphen!)
              # 'sphinxcontrib.asciinema', # enables links to asciicasts from the doc.
              # 'sphinxcontrib.confluencebuilder',
              ]


templates_path = ['_templates']
source_suffix = ['.rst', 'md']
exclude_patterns = ['_build',
                    'Thumbs.db',
                    '.DS_Store',
                    ]
# -- Options for HTML output
pygments_style = "friendly"
html_theme = 'furo'
# html_theme = "furo"  # python3 -m pip install furo
html_static_path = ['_static']
