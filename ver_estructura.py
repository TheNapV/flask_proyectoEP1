import sqlite3

# Conectarse a tu base de datos actual
with sqlite3.connect('database.db') as conn:
    cursor = conn.cursor()
    
    # --- Consultar la estructura de la tabla 'productos' ---
    cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='productos'")
    estructura_productos = cursor.fetchone()
    
    print("Estructura de la tabla PRODUCTOS:")
    print("---------------------------------")
    print(estructura_productos[0]) 
    
    print("\n") # Esto imprime un salto de línea para que no se vea amontonado
    
    # --- Consultar la estructura de la tabla 'usuarios' ---
    cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='usuarios'")
    estructura_usuarios = cursor.fetchone()
    
    print("Estructura de la tabla USUARIOS:")
    print("---------------------------------")
    print(estructura_usuarios[0])