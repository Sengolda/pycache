from setuptools import setup

args = dict(
    name="pycache",
    version="0.1.0b",
    description="A set of tools for cache.",
    author="Sengolda",
    license="MIT",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Sengolda/create-a-cli-tool",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
    ],
    include_package_data=True,
    packages=["pycache"],
    package_dir={"": "src"},
    extra_requires={"tests": ["pytest"]},
)

setup(**args)
