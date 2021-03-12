#######################################################################################
#  In the name of God, the Compassionate, the Merciful
#  Pyabr (c) 2020 Mani Jamali. GNU General Public License v3.0
#
#  Official Website: 		http://pyabr.rf.gd
#  Programmer & Creator:    Mani Jamali <manijamali2003@gmail.com>
#  Gap channel: 			@pyabr
#  Gap group:   			@pyabr_community
#  Git source:              github.com/PyFarsi/pyabr
#
#######################################################################################

import setuptools, os

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyabr",
    version="1.2.5",
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
    python_requires='>=3.6',
    setup_requires=['wheel'],
    install_requires=[
        'PyQt5',
        'kivy',
        'pygame',
        'pyqtconsole',
        'requests',
        'PyQtWebEngine',
        'QScintilla',
        'wget',
    ],
    include_package_data=True,
)