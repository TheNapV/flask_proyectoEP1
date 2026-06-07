from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_sesiones'
CORS(app) # Habilitar CORS para cuando lo subas a Vercel/Render

DATABASE = 'database.db'

# ---- CONFIGURACIÓN DE LA BASE DE DATOS ----
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        # Crear tabla de usuarios
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                nombre TEXT
            )
        ''')
        # Crear tabla de productos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                codigo TEXT UNIQUE,
                nombre TEXT,
                descripcion TEXT,
                precio REAL,
                stock INTEGER,
                categoria TEXT
            )
        ''')
        
        # Insertar datos de prueba si la base de datos está vacía
        cursor.execute('SELECT COUNT(*) FROM usuarios')
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO usuarios (username, password, nombre) VALUES ('admin', '1234', 'Administrador del Sistema')")
        
        cursor.execute('SELECT COUNT(*) FROM productos')
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO productos (codigo, nombre, descripcion, precio, stock, categoria) VALUES ('P001', 'Laptop Asus', 'Laptop gamer 16GB RAM, RTX 3060', 4500.50, 15, 'Tecnología')")
            cursor.execute("INSERT INTO productos (codigo, nombre, descripcion, precio, stock, categoria) VALUES ('P002', 'Mouse Logitech', 'Mouse inalámbrico ergonómico', 120.00, 50, 'Accesorios')")
        conn.commit()

init_db() # Ejecutamos la creación al iniciar el servidor

# ---- RUTAS (ENDPOINTS) ----

@app.route('/')
def index():
    return redirect(url_for('login')) # Redirige automáticamente al login

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE username=? AND password=?", (username, password))
            user = cursor.fetchone()
            
            if user:
                session['username'] = username
                session['nombre'] = user[3] # El índice 3 es el campo 'nombre'
                return redirect(url_for('principal'))
            else:
                return render_template('login.html', error="Credenciales incorrectas")
                
    return render_template('login.html')

@app.route('/principal')
def principal():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('principal.html', nombre=session['nombre'])

@app.route('/buscador')
def buscador():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('buscador.html')

@app.route('/api/buscar_producto', methods=['POST'])
def buscar_producto():
    data = request.get_json()
    codigo = data.get('codigo')
    
    with sqlite3.connect(DATABASE) as conn:
        conn.row_factory = sqlite3.Row # Para poder acceder a las columnas por nombre
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE codigo=?", (codigo,))
        producto = cursor.fetchone()
        
        if producto:
            return jsonify(dict(producto)), 200
        else:
            return jsonify({'error': 'Producto no encontrado'}), 404

@app.route('/logout')
def logout():
    session.clear() # Cierra la sesión
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)