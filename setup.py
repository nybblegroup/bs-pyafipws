from setuptools import setup, find_packages

setup(
    name="pyafipws",  # Nuevo nombre para evitar conflictos
    version="3.6.0-nybble",  # Version personalizada para V11
    description="Fork del cliente AFIP de Reingart, mantenido por NybbleGroup",
    long_description="Versión personalizada del paquete PyAfipWs, con cambios específicos aplicados por NybbleGroup.",
    author="Mariano Reingart",
    author_email="reingart@gmail.com",
    license="GNU GPL v3+",
    url="https://github.com/nybblegroup/bs-pyafipws",  # O tu fork si querés
    packages=find_packages(),
    python_requires='>=3.6',
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.6",
        "Natural Language :: Spanish",
    ],
)
