# PyAfipWs - Versión Nybble Group

Esta es una versión modificada de PyAfipWs mantenida por Nybble Group, basada en el trabajo original de Mariano Reingart.

## Instalación

### Desde el repositorio de Nybble Group

Para instalar esta versión específica y evitar conflictos con la versión publicada en PyPI:

```bash
pip install git+https://github.com/nybblegroup/bs-pyafipws.git#egg=PyAfipWs
```

### Usando requirements.txt

Crea un archivo `requirements.txt` con el siguiente contenido:

```txt
# Dependencias principales
httplib2>=0.12.0
git+https://github.com/pysimplesoap/pysimplesoap.git@stable_py3k#pysimplesoap
m2crypto>=0.18
fpdf>=1.7.2
dbf>=0.88.019
Pillow>=2.0.0
certifi>=2020.4.5.1

# PyAfipWs desde el repositorio de nybblegroup
git+https://github.com/nybblegroup/bs-pyafipws.git#egg=PyAfipWs
```

Luego instala:

```bash
pip install -r requirements.txt
```

## Diferencias con la versión original

- **Versión**: Usa el prefijo "nybble" para evitar conflictos con PyPI
- **Repositorio**: Apunta a `https://github.com/nybblegroup/bs-pyafipws`
- **Compatibilidad**: Mejorada para Python 3.8+
- **Configuración**: Incluye archivos de configuración modernos (`pyproject.toml`, `setup.cfg`)

## Uso

El uso es idéntico al PyAfipWs original. Todos los módulos y funcionalidades están disponibles:

```python
from pyafipws import wsaa, wsfev1, wslpg, wsctg
# ... resto del código igual que en la versión original
```

## Desarrollo

Para contribuir o desarrollar:

```bash
# Clonar el repositorio
git clone https://github.com/nybblegroup/bs-pyafipws.git
cd bs-pyafipws

# Instalar en modo desarrollo
pip install -e .

# Instalar dependencias de desarrollo
pip install -e ".[dev]"
```

## Licencia

Este proyecto mantiene la licencia GPL v3+ del proyecto original.

## Créditos

- **Autor original**: Mariano Reingart (reingart@gmail.com)
- **Mantenimiento**: Nybble Group
- **Repositorio original**: https://github.com/reingart/pyafipws 