#!/usr/bin/python
# -*- coding: latin-1 -*-

"""
Setup script for PyAfipWs - Nybble Group version
"""

import os
import glob
from setuptools import setup, find_packages

# Read version from __init__.py
with open('__init__.py', 'r', encoding='latin-1') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.split('=')[1].strip().strip('"\'')
            break
    else:
        version = "nybble.1.0.dev"

# Read README
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

# Find all Python files
python_files = glob.glob('*.py')
data_files = []

# Add configuration files
if os.path.exists('conf'):
    data_files.extend(glob.glob('conf/*'))

# Add template files
if os.path.exists('plantillas'):
    data_files.extend(glob.glob('plantillas/*'))

# Add data files
if os.path.exists('datos'):
    data_files.extend(glob.glob('datos/*'))

setup(
    name="PyAfipWs",
    version=version,
    description="Interfases, tools and apps for Argentina's gov't. webservices (soap, com/dll, pdf, dbf, xml, etc.)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Mariano Reingart",
    author_email="reingart@gmail.com",
    maintainer="Nybble Group",
    maintainer_email="info@nybblegroup.com",
    url="https://github.com/nybblegroup/bs-pyafipws",
    license="GNU GPL v3+",
    packages=find_packages(),
    py_modules=[
        'wsaa', 'wsfev1', 'wsfexv1', 'wsbfev1', 'wsmtx', 'wsct', 'wsctg', 
        'wslpg', 'wsltv', 'wslum', 'wslsp', 'wsremcarne', 'wscoc', 'wscdc',
        'ws_sr_padron', 'cot', 'iibb', 'trazamed', 'trazaprodmed', 'trazarenpre',
        'trazafito', 'trazavet', 'padron', 'sired', 'pyfepdf', 'pyemail', 
        'pyi25', 'pyrece', 'rece1', 'receb1', 'recex1', 'recem', 'recet',
        'rg3685', 'utils', 'wdigdepfiel'
    ],
    include_package_data=True,
    package_data={
        '': ['*.py', '*.ini', '*.crt', '*.key', '*.tlb', '*.idl'],
        'pyafipws': [
            'plantillas/*',
            'conf/*',
            'datos/*',
            'ejemplos/*',
            'formatos/*',
            'src/*',
            'tests/*',
            'typelib/*'
        ]
    },
    python_requires=">=3.6",
    install_requires=[
        "httplib2>=0.12.0",
        "m2crypto>=0.18",
        "fpdf>=1.7.2",
        "dbf>=0.88.019",
        "Pillow>=2.0.0",
        "certifi>=2020.4.5.1",
    ],
    extras_require={
        'dev': [
            'pytest>=6.0',
            'pytest-cov>=2.0',
            'black>=21.0',
            'flake8>=3.8',
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Operating System :: Microsoft :: Windows",
        "Natural Language :: Spanish",
        "Topic :: Office/Business :: Financial :: Point-Of-Sale",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Object Brokering",
    ],
    keywords="webservice electronic invoice pdf traceability",
    project_urls={
        "Homepage": "https://github.com/nybblegroup/bs-pyafipws",
        "Repository": "https://github.com/nybblegroup/bs-pyafipws",
        "Documentation": "https://github.com/nybblegroup/bs-pyafipws#readme",
        "Bug Tracker": "https://github.com/nybblegroup/bs-pyafipws/issues",
    },
) 