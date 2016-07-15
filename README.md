# drake
Ecuación de Drake en python.

### Requisitos preliminares

  1. Instala Python.

[Python](https://es.wikipedia.org/wiki/Python) es un lenguaje de programación multiplataforma de código abierto, y es muy usado en la comunidad científica.

Muchas distribuciones de Macintosh, Linux y Windows vienen con Python preinstalado. Para comprobar si tienes alguna versión de Python instalada, desde la Terminal (en Mac o Linux) o desde Símbolo del Sistema (Windows) escribe:

```bash
python -c "print('Hola mundo')"
```

Si tienes algún error con esto, tendrás que instalar Python manualmente. Si eres un principiante en lenguajes de programación, lo más fácil será que descarges una distribución como [Anaconda](https://www.continuum.io/downloads), que incluye varios de los paquetes más populares para análisis numérico.
Si ya eres un programador experto, puedes obtener la versión más actual de Python para tu sistema operativo [aquí](https://www.python.org/downloads/). 

En Hipótesis Nula recomendamos usar Python 2.7, pero trataremos de hacer nuestro código compatible con Python 3.

  2. Instala Numpy.

Numpy es una librería de Python que incluye varias funciones matemáticas útiles para hacer análisis numérico.

Si tu sistema operativo ya venía con Python instalado, o si lo instalaste usando Anaconda, es muy probable que ya tengas numpy. Para probar esto escribiendo en la línea de comando 

```bash
python -c "import numpy; print numpy.__version__"
```
De otra forma, puedes seguir las instrucciones especificadas en la [aquí](http://scipy.org/install.html).

  3. (Opcional) Instala [Git](https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Instalación-de-Git).
  
  4. Descarga el repositorio.
  
Puedes descargar el repositorio directamente como archivo zip y descomprimirlo en la ubicación deseada.
Alternativamente, si decides usar Git, desde la línea de comando puedes clonar el repositorio:
```bash
cd <ubicación deseada>
git clone https://github.com/hipotesisnula/drake.git
```

Esto creará una carpeta llamada `drake` en tu ubicación deseada

### Instructivo de uso

##### Modo interactivo
Puedes correr el código directamente escribiendo en la línea de comando

```bash
cd <ubicación de la carpeta drake>
python drake_ep.py
````

**Tip**: En Mac y Linux, después de abrir la terminal, puedes escribir `cd` y después arrastrar directamente la carpeta `drake` a la terminal.

##### Usando un archivo de entrada
En el archivo `factores.csv` se encuentran los estimados originales de Drake para las variables de su ecuación. Tú puedes escribir tus propios estimados en este archivo, y usarlo como argumento de entrada para el script principal. Para esto puedes escribir en la terminal:

```bash
cd <ubicación de la carpeta drake>
python drake_eq.py -factores factores.csv
```

¡Esperamos que te diviertas estimando el número de civilizaciones extraterrestres en nuestra galaxia!




