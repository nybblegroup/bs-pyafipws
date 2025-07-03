# Instrucciones de Instalación - PyAfipWs Nybble Group

## Problema Resuelto

El error que estabas experimentando se debía a que `setuptools_scm` intentaba escribir un archivo de versión en `pyafipws/_version.py`, pero ese directorio no existía en la estructura del proyecto.

## Solución Implementada

He simplificado la configuración del proyecto para que funcione correctamente con instalación desde Git:

### Cambios Realizados:

1. **setup.py simplificado**: Eliminé la dependencia de `setuptools_scm` y creé una versión más simple
2. **pyproject.toml actualizado**: Removí `setuptools_scm` de las dependencias de build
3. **setup.cfg mejorado**: Configuración más compatible
4. **__init__.py actualizado**: Incluye la versión y metadatos correctos

### Archivos Creados/Modificados:

- ✅ `setup.py` - Versión simplificada
- ✅ `pyproject.toml` - Sin setuptools_scm
- ✅ `setup.cfg` - Configuración mejorada
- ✅ `__init__.py` - Con versión nybble
- ✅ `MANIFEST.in` - Para incluir archivos
- ✅ `requirements.txt` - Actualizado
- ✅ `requirements-nybble.txt` - Ejemplo de uso

## Cómo Instalar

### Opción 1: Desde requirements.txt

```bash
pip install -r requirements.txt
```

### Opción 2: Directamente desde Git

```bash
pip install git+https://github.com/nybblegroup/bs-pyafipws.git@main#egg=PyAfipWs
```

### Opción 3: Clonar y instalar

```bash
git clone https://github.com/nybblegroup/bs-pyafipws.git
cd bs-pyafipws
pip install -e .
```

## Verificación

Para verificar que la instalación funcionó correctamente:

```python
import pyafipws
print(pyafipws.__version__)  # Debería mostrar "nybble.1.0.dev"
```

## Estructura del Proyecto

```
bs-pyafipws/
├── setup.py              # Setup simplificado
├── pyproject.toml        # Configuración moderna
├── setup.cfg            # Configuración adicional
├── __init__.py          # Con versión nybble
├── requirements.txt     # Dependencias
├── MANIFEST.in         # Archivos a incluir
└── *.py                # Módulos de PyAfipWs
```

## Beneficios de la Nueva Configuración

1. **Sin conflictos**: Versión con prefijo "nybble" evita conflictos con PyPI
2. **Instalación simple**: Funciona directamente desde Git
3. **Compatibilidad**: Soporta Python 3.6+
4. **Mantenimiento**: Fácil de actualizar y mantener

## Troubleshooting

Si sigues teniendo problemas:

1. **Limpiar cache de pip**:
   ```bash
   pip cache purge
   ```

2. **Forzar reinstalación**:
   ```bash
   pip install --force-reinstall git+https://github.com/nybblegroup/bs-pyafipws.git@main#egg=PyAfipWs
   ```

3. **Usar versión específica**:
   ```bash
   pip install git+https://github.com/nybblegroup/bs-pyafipws.git@<commit-hash>#egg=PyAfipWs
   ```

## Notas Importantes

- El nombre del paquete se mantiene como "PyAfipWs"
- La versión usa el prefijo "nybble" para evitar conflictos
- Todos los módulos originales están disponibles
- La funcionalidad es idéntica al PyAfipWs original 