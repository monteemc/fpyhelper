import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fpyhelper-monteemc",
    version="0.0.1",
    author="MonteEMC",
    author_email="mtegit@fastmail.com",
    description="Functional programing auxiliary functions in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/monteemc/fpyhelper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)