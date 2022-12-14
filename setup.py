import os

from setuptools import find_packages, setup

VERSION = "{{VERSION_PLACEHOLDER}}"  # Version will be replaced by the CI/CD pipeline

if VERSION.startswith("{{"):
    VERSION = "0.0.0"


def get_readme() -> str:
    """Load the contents of the README file"""
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    with open(readme_path, "r") as f:
        return f.read()


def get_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()


setup(
    name="aiogram-di",
    description="",
    long_description=get_readme(),
    long_description_content_type="text/markdown",
    version=VERSION,
    packages=find_packages(include=["aiogram-di"]),
    url="https://github.com/MaximZayats/aiogram-di",
    author="Maxim",
    author_email="maximzayats1@gmail.com",
    install_requires=get_requirements(),
    keywords=[
        "python",
        "aiogram",
        "di",
        "dependency injection",
        "aiogram di",
    ],
)
