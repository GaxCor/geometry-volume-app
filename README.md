# geometry-volume-app

Este proyecto es una aplicación sencilla en Python para calcular el volumen de diferentes figuras geométricas en 3D, como cajas, conos, cilindros y esferas.  
Además del cálculo, el proyecto incluye pruebas unitarias para verificar que las funciones se comporten correctamente en distintos escenarios.

## Estructura del proyecto

geometry-volume-app/
├─ geometry/
│ ├─ init.py
│ ├─ box.py
│ ├─ cone.py
│ ├─ cylinder.py
│ └─ sphere.py
├─ tests/
│ ├─ init.py
│ ├─ test_box.py
│ ├─ test_cone.py
│ ├─ test_cylinder.py
│ └─ test_sphere.py
├─ main.py
├─ requirements.txt
└─ README.md

markdown
Copiar código

- `geometry/` contiene las funciones que calculan el volumen de cada figura.
- `tests/` incluye las pruebas unitarias realizadas con `pytest`.
- `main.py` permite ejecutar un ejemplo sencillo del proyecto.

## Cómo ejecutar el programa

Desde la carpeta raíz del proyecto, ejecutar:

```bash
python main.py
Cómo ejecutar las pruebas
Desde la carpeta raíz del proyecto, ejecutar:

bash
Copiar código
pytest
Esto ejecuta todas las pruebas unitarias definidas en la carpeta tests.

Dependencias
Para instalar las dependencias necesarias, ejecutar:

bash
Copiar código
pip install -r requirements.txt
La única dependencia externa utilizada en este proyecto es pytest, que se usa para realizar las pruebas unitarias.

css
Copiar código
```
