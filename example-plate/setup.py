from setuptools import setup, find_packages

setup(
    name="example_plate",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    package_data={"example_plate": ["example_plate/static/example_plate.css"]},
    description="Sphinx extension for custom admonition",
    author="Dmitriy Belkin",
    author_email="demetrius.belkin@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Documentation",
        "Framework :: Sphinx :: Extension",
    ],
)