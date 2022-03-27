from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="xcash",
    version="0.2.0",
    packages=find_packages(),
    description="XCASH Foundation ecosystem API wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/X-CASH-official/XCASH-Ecosystem-api-wrapper",
    author="AnimusXCASH",
    author_email="lovro@xcash.foundation",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    install_requires=[
        "requests"
    ],
)
