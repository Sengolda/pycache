from setuptools import setup

args = dict(
    name = "pycache",
    version="0.1.0b",
    description = "A set of tools for cache.",
    author = "Sengolda",
    license = "MIT",
    long_description = open("README.rst", "r", encoding="utf-8").read(),
    long_description_content_type = "text/x-rst",
    url = "https://github.com/pyscaffold/pyscaffold/",
    classifiers = [
    "Development Status :: 4 - Beta",
    "Programming Language :: Python :: 3",
    ],
    include_package_data = True,
    packages = ["pycache"],
    package_dir = {'': 'src'},
)

setup(**args)
