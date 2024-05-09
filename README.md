
# Blackbuda

## Descripción
Este código realiza análisis de datos. El proceso incluye la carga, limpieza, y análisis de datos para obtener insights relevantes en el cuestionario entregado.

## Cálculos realizados
Para más detalles sobre las fórmulas y la lógica utilizada para esta prueba, consulta el notebook `Buda.ipynb`. pero, si deseas ejecutar el código consulta la instalación.


## Instalación
Sigue estos pasos para instalar las librerías necesarias:

```bash
# Crea un entorno virtual
python -m venv venv

# Activa el entorno virtual
# En sistemas Unix o MacOS
source venv/bin/activate

# En Windows
source venv/Scripts/activate

# Instala las dependencias
pip install -r requirements.txt
```

## Uso
Para ejecutar el código, utiliza el siguiente comando:

```bash
python .\buda.py
```

##Troubleshooting
Si tienes un error como *cannot import name 'appengine' from 'requests.packages.urllib3.contrib'* entonces:
```bash
pip install --upgrade requests-toolbelt
```
y vuelve a ejecutar :)
