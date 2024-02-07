import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ggim",
    author="Lukas Halbritter",
    author_email="halbi93@gmx.de",
    description="A tool for drawing beautiful and expressive git graphs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classfiers=[
        "Development Status :: 2 - Pre-Alpha" "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
