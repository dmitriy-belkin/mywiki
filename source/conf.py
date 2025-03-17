# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MyWiki'
copyright = '2025, Dmitriy Belkin'
author = 'Dmitriy Belkin'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 'sphinx_design', 'sphinxcontrib.plantuml', 'sphinx_copybutton']
myst_enable_extensions = {
    'colon_fence',
    'tasklist',
    'attrs_block',
    'attrs_inline',
    'linkify',
    'fieldlist',
}

plantuml = 'java -jar /docs/plantuml.jar' # поддержка PlantUML

templates_path = ['_templates']

exclude_patterns = ['_includes/*']

language = 'ru'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'

html_theme_options = {
    "repository_url": "https://github.com/dmitriy-belkin/mywiki",
    # "use_repository_button": True,
    # "use_edit_page_button": True,
    # "show_navbar_depth": 2,
    # "use_fullscreen_button": False,
    "home_page_in_toc": True,
    "toc_title": " На этой странице:",
    "article_header_start": "breadcrumbs", # хлебные крошки в хедере
    "max_navbar_depth": 3, # регулирует глубину содержания в левом навбаре
    "show_toc_level": 4, # регулирует глубину содержания в правом навбаре

}

html_css_files = ["css/custom.css"]

html_static_path = ['_static']

#custom css
html_show_sphinx = 0
html_favicon = '_static/favicon.ico'
html_logo = '_static/logo.png'
