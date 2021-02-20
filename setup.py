from setuptools import setup, find_packages
from os import path

README_MD = open(path.join(path.dirname(path.abspath(__file__)), "README.md")).read()

setup(
    name="donttrust",
    version="0.1.4",
    description="Form validation library for python",
    long_description=README_MD,
    long_description_content_type="text/markdown",
    url="https://github.com/arnu515/donttrust",
    author="arnu515",
    author_email="arnu5152@gmail.com",
    keywords="form validation trust joi",
    license="MIT",
    packages=find_packages(exclude=(
        "tests",
    )),
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Typing :: Typed"
    ],
)
