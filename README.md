=======================================================================
SISTEMA WEB CON FLASK — EXAMEN PARCIAL (PREGUNTA 1)
=======================================================================
Curso: Programación Aplicada II
Autor: Joseph Andree Flores Saavedra
Tecnologías: Flask, SQLite, HTML5, CSS3, JavaScript

=======================================================================
1. DESCRIPCIÓN DEL PROYECTO
=======================================================================
Esta aplicación web utiliza el patrón MVC e implementa un sistema de 
acceso mediante login. Si las credenciales son correctas, el 
usuario accede a un panel principal y a un buscador de productos por 
código. El backend procesa la base de datos SQLite y el 
frontend renderiza los datos utilizando peticiones asíncronas (Fetch API).

=======================================================================
2. ESTRUCTURA DE ARCHIVOS Y CARPETAS
=======================================================================
flask_proyecto/
  ├── app.py                 # Enrutador principal y API del backend
  ├── database.db            # Base de datos SQLite (Autogenerada)
  ├── requirements.txt       # Dependencias (Flask, Flask-Cors, gunicorn)
  ├── ver_estructura.py      # Script auxiliar para ver código SQL de tablas
  └── templates/             # Vistas del frontend (HTML)
        ├── login.html       # Interfaz de inicio de sesión
        ├── principal.html   # Panel de bienvenida y menú
        └── buscador.html    # Buscador asíncrono con Fetch API

=======================================================================
3. ENLACES DE PRODUCCIÓN (DESPLIEGUE)
=======================================================================
El proyecto ha sido desplegado exitosamente separando el entorno:

- Frontend (Vercel): https://flask-proyecto-ep-1.vercel.app/login.html
- Backend y API (Render): https://examenparcial01pa2-jfs.onrender.com

*Nota: Para probar el funcionamiento completo del sistema con el manejo 
de sesiones de Flask de manera óptima, se recomienda utilizar el enlace 
del Backend alojado en Render.*

=======================================================================
4. CÓMO EJECUTAR EL PROYECTO LOCALMENTE
=======================================================================
Para probar la aplicación en tu computadora, sigue estos pasos:

1. Abrir la terminal en la carpeta del proyecto e instalar dependencias:
   > pip install -r requirements.txt

2. Iniciar el servidor local:
   > python app.py

3. Abrir el navegador e ingresar a la dirección:
   > http://localhost:5000

DATOS DE PRUEBA:
- Usuario: admin
- Contraseña: 1234
- Códigos de búsqueda: P001, P002

=======================================================================
5. INSTRUCCIONES DE DESPLIEGUE REALIZADAS
=======================================================================
A. Despliegue del Backend en RENDER:
   1. Se conectó el repositorio de GitHub a un nuevo "Web Service".
   2. Comando de Build configurado: pip install -r requirements.txt.
   3. Comando de Start configurado: gunicorn app:app.
   4. Se habilitó la librería CORS en el archivo app.py.

B. Despliegue del Frontend en VERCEL:
   1. Se importó el repositorio desde GitHub a un nuevo proyecto.
   2. Se seleccionó la carpeta /templates como "Root Directory".
   3. En Variables de Entorno, se creó "BACKEND_URL" apuntando a la 
      API de Render.

=======================================================================
6. ESTRUCTURA DE LA BASE DE DATOS (SQLITE)
=======================================================================
El sistema autogenera el archivo database.db. Su estructura puede 
verificarse ejecutando el script "ver_estructura.py":

TABLA USUARIOS:
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT,
    nombre TEXT
)

TABLA PRODUCTOS:
CREATE TABLE productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo TEXT UNIQUE,
    nombre TEXT,
    descripcion TEXT,
    precio REAL,
    stock INTEGER,
    categoria TEXT
)
