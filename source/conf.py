# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'mywiki'
copyright = '2025, Dmitriy Belkin'
author = 'Dmitriy Belkin'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'

html_theme_options = {
    "repository_url": "https://github.com/dmitriy-belkin/mywiki",
    "use_repository_button": True,
    "use_edit_page_button": True,
    "show_navbar_depth": 2,
    "use_fullscreen_button": False,
    "home_page_in_toc": True,
    "show_toc_level": 2,
}

html_static_path = ['_static']

#custom css
html_title = "My Wiki"
