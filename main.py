import random 

class Producto:
    def __init__(self, categoria, nombre_prod, precio, cantidad):
        self.id = random.randint(1, 9999999)
        self.categoria = categoria
        self.nombre_prod = nombre_prod
        self.precio = precio
        self.cantidad = cantidad

class ProductoElectronico(Producto):
    def __init__(self, categoria, nombre_prod, precio, cantidad, voltaje, consumo_energetico):
        super().__init__(categoria, nombre_prod, precio, cantidad)
        self.voltaje = voltaje
        self.consumo_energetico = consumo_energetico

class ProductoAlimenticio(Producto):
    def __init__(self, categoria, nombre_prod, precio, cantidad, fecha_vencimiento):
        super().__init__(categoria, nombre_prod, precio, cantidad)
        self.fecha_vencimiento = fecha_vencimiento

class Inventario:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def buscar_producto(self, id):
        for producto in self.productos:
            if producto.id == id:
                return producto
        return None
            
    def eliminar_producto(self, id):
        producto = self.buscar_producto(id)
        if producto:
            self.productos.remove(producto)
            print("/////Producto eliminado del inventario/////")
        else:
            print("El producto no existe\n")
        
    def mostrar_inventario(self):
        productos = self.productos
        tabla_inventario = """\
+--------------------------------------------------------------------------------------------------------+
|ID         Categoria                      Nombre                         Precio          Cantidad       |
|--------------------------------------------------------------------------------------------------------|
{}
+--------------------------------------------------------------------------------------------------------+\
    """
        tabla_inventario = (tabla_inventario.format('\n'.join("|{:<10} {:<30} {:<30} {:<15} {:<15}|".format(
            producto.id, producto.categoria, producto.nombre_prod, producto.precio, producto.cantidad) for producto in productos)))
        print(tabla_inventario)
        
def Menu():
    print("Elija una opcion: \n1. Agregar producto \n2. Eliminar producto \n3. Buscar un producto \n4. Ver inventario completo \n5. Cerrar inventario\n")
    
inventario = Inventario()

while True:
    Menu()
    opcion = int(input())
    if opcion == 1:
        print("Seleccione el tipo de producto: \n1. Producto Consumible \n2. Producto Electronico")
        tipo_producto = int(input())
        
        if tipo_producto != 1 and tipo_producto != 2:
            print("Opción incorrecta\n")
        else:
            nombre = input("Nombre del producto: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            
            if tipo_producto == 1:
                fecha_vencimiento = input("Fecha de vencimiento: ")
                producto = ProductoAlimenticio("Producto Consumible", nombre, precio, cantidad, fecha_vencimiento)
            elif tipo_producto == 2:
                voltaje = input("Voltaje: ")
                consumo_energetico = input("Consumo energético: ")
                producto = ProductoElectronico("Producto Electrónico", nombre, precio, cantidad, voltaje, consumo_energetico)
            
            inventario.agregar_producto(producto)
            print(f"\n/////Producto agregado al inventario///// \nID nuevo producto: {producto.id}\n")
    
    elif opcion == 2:
        print("Ingrese el ID del producto a eliminar:")
        id_eliminar = int(input())
        inventario.eliminar_producto(id_eliminar)
            
    elif opcion == 3:
        print("Ingrese el ID del producto que desea buscar:")
        id_buscar = int(input())
        producto_encontrado = inventario.buscar_producto(id_buscar)
        if producto_encontrado:
            print(f"\n/////Producto encontrado///// \nID: {producto_encontrado.id} \nCategoría: {producto_encontrado.categoria} \nNombre: {producto_encontrado.nombre_prod} \nPrecio: {producto_encontrado.precio} \nCantidad: {producto_encontrado.cantidad}")
            if isinstance(producto_encontrado, ProductoElectronico):
                print(f"Voltaje: {producto_encontrado.voltaje} \nConsumo Energético: {producto_encontrado.consumo_energetico}\n")
            elif isinstance(producto_encontrado, ProductoAlimenticio):
                print(f"Fecha de Vencimiento: {producto_encontrado.fecha_vencimiento}\n")
        else:
            print(f"No se encontró un producto con el ID: {id_buscar}\n")
            
    elif opcion == 4:
        inventario.mostrar_inventario()
    elif opcion == 5:
        break
    else:
        print("Opción incorrecta. Por favor seleccione una opción válida.\n")
