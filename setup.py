from setuptools import setup, find_packages

setup(
    name="bs-pyafipws",  # CAMBIADO para evitar conflicto con el original
    version="1.0.0-nybble",  # Usá lo que corresponda, o podés fijar un commit hash
    description="Fork de PyAfipWs adaptado por NybbleGroup",
    long_description="Versión personalizada del cliente AFIP WS de Reingart, mantenida por NybbleGroup",
    author="NybbleGroup",
    author_email="info@nybblegroup.com",
    url="https://github.com/nybblegroup/bs-pyafipws",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Natural Language :: Spanish"
    ],
    python_requires='>=3.6',
    include_package_data=True,
)
