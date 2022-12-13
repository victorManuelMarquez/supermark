import conexion as bd
import sqlite3 as sql
from tkinter import messagebox as mb


def validar_sesion(app: any, nombre: str, clave: str) -> bool:
    valido = False
    try:
        conexion = bd.Conexion()
        conexion.ejecutar(f'SELECT id, dni, nombre_completo, cliente FROM personas WHERE usuario="{nombre}" AND clave="{clave}" AND activo = 1')
        resultados = conexion.resulset
        valido = len(resultados) > 0
        if valido:
            app.cliente['id'] = resultados[0][0]
            app.cliente['dni'] = resultados[0][1]
            app.cliente['nombre_completo'] = resultados[0][2]
            app.cliente['cliente'] = resultados[0][3]
    except sql.Error as error:
        mb.showerror(title=type(error).__name__, message=str(error))
    finally:
        if conexion:
            conexion.cerrar()
        return valido


def filtrar_productos(valor: str) -> dict:
    matriz = {'cols':[], 'rows':[]}
    try:
        conexion = bd.Conexion()
        conexion.ejecutar(f'SELECT * FROM productos_disponibles WHERE `Detalles` LIKE "%{valor}%"')
        matriz['cols'] = conexion.metadata
        matriz['rows'] = conexion.resulset
    except sql.Error as error:
        mb.showerror(title=type(error).__name__, message=str(error))
    finally:
        if conexion:
            conexion.cerrar()
        return matriz


def finalizar_compra(app: any, articulos: list) -> bool:
    estado = False
    try:
        id = None
        conexion = bd.Conexion()
        estado = conexion.ejecutar(f'''
        INSERT INTO tickets(id_consumidor, id_facilitador) 
        VALUES({app.cliente['id']}, {app.cliente['id']})
        ''') > 0
        if estado:
            conexion.ejecutar(f'''
            SELECT id 
            FROM tickets 
            WHERE 
                id_consumidor = {app.cliente['id']} 
                AND id_facilitador = {app.cliente['id']} 
                AND habilitado = 1
            ORDER BY id DESC LIMIT 1
            ''')
            for resultado in conexion.resulset:
                id = resultado[0]
            else:
                estado = id != None
        if estado:
            for articulo in articulos:
                conexion.ejecutar(f'''
                INSERT INTO ventas(id_ticket, id_producto, cantidad, monto) 
                VALUES({id}, {articulo['ID']}, 1, {articulo['Precio unitario']})
                ''')
                conexion.ejecutar(f'UPDATE productos SET stock = {articulo["Stock"]} WHERE id = {articulo["ID"]}')
        mb.showinfo(title="Éxito", message="¡Venta realizada!")
    except sql.Error as error:
        mb.showerror(title=type(error).__name__, message=str(error))
    finally:
        if conexion:
            conexion.cerrar()
        return estado


def registrar_cliente(datos: dict) -> bool:
    estado = False
    try:
        conexion = bd.Conexion()
        estado = conexion.ejecutar(f'''
        INSERT INTO personas(dni, nombre_completo, usuario, clave) 
        VALUES("{datos['dni']}", "{datos['nombre_completo']}", "{datos['usuario']}", "{datos['clave']}")
        ''') > 0
        mb.showinfo(title="Éxito", message="¡Cliente registrado!")
    except sql.Error as error:
        mb.showerror(title=type(error).__name__, message=str(error))
    finally:
        if conexion:
            conexion.cerrar()
        return estado


def todas_las_personas(valorBuscado: str) -> list:
    resultados = []
    try:
        conexion = bd.Conexion()
        conexion.ejecutar(f'''
        SELECT 
            id, dni, nombre_completo, cliente, activo 
        FROM personas
        WHERE nombre_completo LIKE "%{valorBuscado}%"
        ''')
        for fila in conexion.resulset:
            resultados.append(dict(zip(['id', 'dni', 'nombre_completo', 'cliente', 'activo'], fila)))
    except sql.Error as error:
        mb.showerror(title=type(error).__name__, message=str(error))
    finally:
        if conexion:
            conexion.cerrar()
        return resultados


def actualizar_cliente(cliente: dict) -> bool:
    estado = False
    try:
        conexion = bd.Conexion()
        estado = conexion.ejecutar(f'''
        UPDATE 
            personas 
        SET 
            dni = "{cliente['dni']}", 
            nombre_completo = "{cliente['nombre_completo']}",
            cliente = {int(cliente['cliente'])},
            activo = {int(cliente['activo'])}
        WHERE id = {cliente['id']}
        ''') > 0
        mb.showinfo(title="Éxito", message="¡Persona actualizada!")
    except sql.Error as error:
        mb.showerror(title=type(error).__name__, message=str(error))
    finally:
        if conexion:
            conexion.cerrar()
        return estado


def borrar_cliente(cliente: dict) -> bool:
    estado = False
    try:
        conexion = bd.Conexion()
        estado = conexion.ejecutar(f'UPDATE personas SET activo = 0 WHERE id = {cliente["id"]}') > 0
        mb.showinfo(title="Éxito", message="¡Persona dada de baja!")
    except sql.Error as error:
        mb.showerror(title=type(error).__name__, message=str(error))
    finally:
        if conexion:
            conexion.cerrar()
        return estado


def todas_las_categorias() -> list:
    resultados = []
    try:
        conexion = bd.Conexion()
        conexion.ejecutar(f'SELECT nombre FROM categorias ORDER BY nombre')
        for fila in conexion.resulset:
            resultados.append(fila[0])
    except sql.Error as error:
        mb.showerror(title=type(error).__name__, message=str(error))
    finally:
        if conexion:
            conexion.cerrar()
        return resultados


def id_categoria(valorBuscado: str) -> any:
    id = None
    try:
        conexion = bd.Conexion()
        conexion.ejecutar(f'SELECT id FROM categorias WHERE nombre = "{valorBuscado}" LIMIT 1')
        id = conexion.resulset[0][0]
    except sql.Error as error:
        mb.showerror(title=type(error).__name__, message=str(error))
    finally:
        if conexion:
            conexion.cerrar()
        return id


def registrar_producto(datos: dict) -> bool:
    estado = False
    try:
        conexion = bd.Conexion()
        estado = conexion.ejecutar(f'''
        INSERT INTO productos(id_categoria, descripcion, precio, stock)
        VALUES({datos['id_categoria']}, "{datos['descripcion']}", {float(datos['precio'])}, {int(datos['stock'])})
        ''') > 0
        mb.showinfo(title="Éxito", message="¡Producto registrado!")
    except sql.Error as error:
        mb.showerror(title=type(error).__name__, message=str(error))
    finally:
        if conexion:
            conexion.cerrar()
        return estado


def todos_los_productos() -> list:
    resultados = []
    try:
        conexion = bd.Conexion()
        conexion.ejecutar('SELECT * FROM productos')
        for fila in conexion.resulset:
            resultados.append(dict(zip(
                ['id', 'id_categoria', 'descripcion', 'precio', 'stock', 'activo'], 
                fila
            )))
    except sql.Error as error:
        mb.showerror(title=type(error).__name__, message=str(error))
    finally:
        if conexion:
            conexion.cerrar()
        return resultados


def nombre_categoria(id: str) -> any:
    nombre = None
    try:
        conexion = bd.Conexion()
        conexion.ejecutar(f'SELECT nombre FROM categorias WHERE id = {id} LIMIT 1')
        nombre = conexion.resulset[0][0]
    except sql.Error as error:
        mb.showerror(title=type(error).__name__, message=str(error))
    finally:
        if conexion:
            conexion.cerrar()
        return nombre


def actualizar_producto(datos: dict) -> bool:
    estado = False
    try:
        conexion = bd.Conexion()
        estado = conexion.ejecutar(f'''
        UPDATE productos 
        SET 
            id_categoria = {datos['id_categoria']},
            descripcion = "{datos['descripcion']}",
            precio = {float(datos['precio'])},
            stock = {int(datos['stock'])},
            activo = {int(datos['activo'])}
        WHERE id = {datos['id']}
        ''') > 0
        mb.showinfo(title="Éxito", message="¡Producto actualizado!")
    except sql.Error as error:
        mb.showerror(title=type(error).__name__, message=str(error))
    finally:
        if conexion:
            conexion.cerrar()
        return estado


def borrar_producto(datos: dict) -> bool:
    estado = False
    try:
        conexion = bd.Conexion()
        estado = conexion.ejecutar(f'UPDATE productos SET activo = 0 WHERE id = {datos["id"]}') > 0
        mb.showinfo(title="Éxito", message="¡Producto eliminado!")
    except sql.Error as error:
        mb.showerror(title=type(error).__name__, message=str(error))
    finally:
        if conexion:
            conexion.cerrar()
        return estado


def registrar_categoria(nombre: str) -> bool:
    estado = False
    try:
        conexion = bd.Conexion()
        estado = conexion.ejecutar(f'INSERT INTO categorias(nombre) VALUES("{nombre}")') > 0
        mb.showinfo(title="Éxito", message="¡Categoría registrada!")
    except sql.Error as error:
        mb.showerror(title=type(error).__name__, message=str(error))
    finally:
        if conexion:
            conexion.cerrar()
        return estado


def actualizar_categoria(nombre: str, nombre_nuevo: str) -> bool:
    estado = False
    try:
        conexion = bd.Conexion()
        estado = conexion.ejecutar(f'UPDATE categorias SET nombre = "{nombre_nuevo}" WHERE nombre = "{nombre}"') > 0
        mb.showinfo(title="Éxito", message="¡Categoría actualizada!")
    except sql.Error as error:
        mb.showerror(title=type(error).__name__, message=str(error))
    finally:
        if conexion:
            conexion.cerrar()
        return estado


def compras_cliente(cliente: dict) -> dict:
    matriz = {'cols':[], 'rows':[]}
    try:
        conexion = bd.Conexion()
        conexion.ejecutar(f'''
        SELECT `Ticket`, `Cliente`, `Vendedor`, `Fecha de compra`, `Producto`, `Cantidad`, `Precio Final` 
        FROM ventas_detalles INNER JOIN tickets ON tickets.id = ventas_detalles.`Ticket`
        WHERE id_consumidor = {cliente["id"]}
        ''')
        matriz['cols'] = conexion.metadata
        matriz['rows'] = conexion.resulset
    except sql.Error as error:
        mb.showerror(title=type(error).__name__, message=str(error))
    finally:
        if conexion:
            conexion.cerrar()
        return matriz


def todas_las_ventas_de() -> dict:
    matriz = {'cols':[], 'rows':[]}
    try:
        conexion = bd.Conexion()
        conexion.ejecutar(f'SELECT * FROM ventas_detalles')
        matriz['cols'] = conexion.metadata
        matriz['rows'] = conexion.resulset
    except sql.Error as error:
        mb.showerror(title=type(error).__name__, message=str(error))
    finally:
        if conexion:
            conexion.cerrar()
        return matriz
