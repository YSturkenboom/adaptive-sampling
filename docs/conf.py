#!/usr/bin/env python
#
# direct documentation build configuration file, created by
# sphinx-quickstart on Fri Jun  9 13:47:02 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another
# directory, add these directories to sys.path here. If the directory is
# relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
#
import os
import sys
import mock
from typing import Dict, List, Tuple, Optional, Callable

# to support markdown
from recommonmark.parser import CommonMarkParser

sys.path.insert(0, os.path.abspath("../"))


# Mock imports
try:
    import torch  # noqa
except ImportError:
    for m in [
        "torch",
        "torch.nn",
        "torch.nn.parallel",
        "torch.distributed",
        "torch.multiprocessing",
        "torch.autograd",
        "torch.autograd.function",
        "torch.nn.modules",
        "torch.nn.modules.utils",
        "torch.utils",
        "torch.utils.data",
    ]:
        sys.modules[m] = mock.Mock(name=m)
    sys.modules["torch"].__version__ = "1.5"  # fake version

import direct  # noqa


# -- General configuration ---------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
needs_sphinx = "3.0"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "recommonmark",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "sphinx.ext.doctest",
    "sphinx.ext.autosummary",
    "sphinx.ext.autosectionlabel",
]


# Plugin config
napoleon_google_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_special_with_doc = True
napoleon_numpy_docstring = True
napoleon_use_rtype = False
autodoc_inherit_docstrings = False
autodoc_member_order = "bysource"
autosummary_generate = True
numpydoc_show_class_members = False

# Do not throw warnings for duplicated section names in different documents.
autosectionlabel_prefix_document = True

intersphinx_mapping = {
    "python": ("https://docs.python.org/3.6", None),
    "numpy": ("https://docs.scipy.org/doc/numpy/", None),
    "torch": ("https://pytorch.org/docs/master/", None),
}

todo_include_todos = True


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_parsers = {
    ".rst": "restructuredtext",
    ".md": CommonMarkParser,
}
source_suffix = [".rst", ".md"]


# The master toctree document.
master_doc = "index"

# General information about the project.
project = "DIRECT"
copyright = "2020, Jonas Teuwen"
author = "DIRECT Contributors"

# The version info for the project you're documenting, acts as replacement
# for |version| and |release|, also used in various other places throughout
# the built documents.
#
# The short X.Y version.
version = direct.__version__
# The full version, including alpha/beta/rc tags.
release = direct.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output -------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_theme_path = [
    "_themes",
]

# Theme options are theme-specific and customize the look and feel of a
# theme further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


# -- Options for HTMLHelp DoIterationOutput ---------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "directdoc"


# -- Options for LaTeX DoIterationOutput ------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto, manual, or own class]).
latex_documents = [
    (master_doc, "direct.tex", "DIRECT Documentation", "Jonas Teuwen", "manual"),
]


# -- Options for manual page DoIterationOutput ------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "direct", "DIRECT Documentation", [author], 1)]


# -- Options for Texinfo DoIterationOutput ----------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "direct",
        "DIRECT Documentation",
        author,
        "direct",
        "One line description of project.",
        "Miscellaneous",
    ),
]


def setup(app):
    from recommonmark.transform import AutoStructify

    app.add_config_value(
        "recommonmark_config",
        {
            "auto_toc_tree_section": "Contents",
            "enable_math": True,
            "enable_inline_math": True,
            "enable_eval_rst": True,
        },
        True,
    )
    app.add_transform(AutoStructify)
