"""Setup script for seoworkflows Pypi package"""

# Standard library imports
import pathlib

# Third party imports
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).resolve().parent

# The text of the README file is used as a description
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="seoworkflows",
    version="1.0.0",
    description="Functions that help power seoworkflows.com",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Jason Melman",
    author_email="jasonm@seoworkflows.com",
    url="https://github.com/jmelm93/seo-workflows-package",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["seoworkflows"],
    include_package_data=True,
    install_requires=["pandas", "yagmail", "pyyaml", "google-cloud-bigquery",  "google-api-python-client",  "xlsxwriter", "sklearn", ],
    entry_points={"console_scripts": ["seoworkflows=seo_workflows.__main__:main"]},
)