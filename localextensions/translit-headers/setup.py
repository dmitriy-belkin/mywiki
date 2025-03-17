from setuptools import setup, find_packages

setup(
    name="translit-headers",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'Unidecode',
    ],
    description="Sphinx extension for header transliteration",
    author="Dmitriy Belkin",
    author_email="demetrius.belkin@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Documentation",
        "Framework :: Sphinx :: Extension",
    ],
)