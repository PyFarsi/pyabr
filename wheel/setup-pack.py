'''
    Pyabr OS

    Python Cloud Operating System Platform (c) 2021 PyFarsi. Free Software GNU General Public License v3.0

    - Informations

    * Name:             Pyabr
    * Founder:          Mani Jamali
    * Developers:       PyFarsi Community
    * Package Manager:  Paye, PyPI
    * License:          GNU General Publice License v3.0

    - Official Website

    * Persian Page:     https://pyabr.ir
    * English Page:     https://en.pyabr.ir
'''

import setuptools, os

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyabr",
    version="2.2.0",
    author="Mani Jamali",
    author_email="pyabrsystem@gmail.com",
    description="Python Cloud & OS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PyFarsi/pyabr",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.7',
    setup_requires=['wheel'],
    install_requires=[
        'PyQt5',
        'requests',
        'cryptography',
        'termcolor',
        'wget',
    ],
    include_package_data=True,
)