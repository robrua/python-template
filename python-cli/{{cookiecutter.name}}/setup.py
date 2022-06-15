#!/usr/bin/env python
from pathlib import Path

from setuptools import find_packages, setup

install_requires = ["click"]

version_file = Path(__file__).parent.joinpath(
    "{{cookiecutter.module_name}}", "VERSION.txt"
)
version = version_file.read_text(encoding="UTF-8").strip()

with open("README.md", "r", encoding="UTF-8") as in_file:
    long_description = in_file.read()

setup(
    name="{{cookiecutter.module_name}}",
    version=version,
    author="{{cookiecutter.author_name}}",
    author_email="{{cookiecutter.author_email}}",
    description="{{cookiecutter.description}}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"{{cookiecutter.module_name}}": "{{cookiecutter.module_name}}"},
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "{{cookiecutter.cli_command}}={{cookiecutter.module_name}}.__main__:{{ cookiecutter.name.replace('-', '_') }}"
        ]
    },
    zip_safe=True,
    python_requires=">=3.9",
    install_requires=install_requires,
    include_package_data=True,
)
