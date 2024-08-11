import random
'''

'''


#----------------------------------------------------------------------------#
################################# CLASE BASE #################################
#----------------------------------------------------------------------------#

# CLASE BASE PRODUCTO
class Producto:
    def __init__(self, categoria, nombre_prod, precio, cantidad):
        
        # USO DE ATRIBUTOS (USO DE ENCAPSULAMIENTO)
        self._id = random.randint(1, 9999999)  # Atributo (encapsulado) para identificar el producto
        self._categoria = categoria  # Atributo (encapsulado) para la categoría del producto
        self._nombre_prod = nombre_prod  # Atributo (encapsulado) para el nombre del producto
        self._precio = precio  # Atributo (encapsulado) para el precio del producto
        self._cantidad = cantidad  # Atributo (encapsulado) para la cantidad de producto en inventario

    # METODOS GETTERS (ACCEDER A ATRIBUTOS PRIVADOS)
    def get_id(self):
        return self._id

    def get_categoria(self):
        return self._categoria

    def get_nombre_prod(self):
        return self._nombre_prod

    def get_precio(self):
        return self._precio

    def get_cantidad(self):
        return self._cantidad

#----------------------------------------------------------------------------#
############################## CLASES HEREDADAS ##############################
#----------------------------------------------------------------------------#

# CLASE PRODUCTOELECTRONICO QUE HEREDA DE PRODUCTO
class ProductoElectronico(Producto):
    def __init__(self, categoria, nombre_prod, precio, cantidad, voltaje, consumo_energetico):
        super().__init__(categoria, nombre_prod, precio, cantidad)  # Herencia y uso de super() para inicializar atributos de la clase base
        self._voltaje = voltaje  # Atributo adicional (encapsulado) para el voltaje del producto electrónico
        self._consumo_energetico = consumo_energetico  # Atributo adicional (encapsulado) para el consumo energético del producto electrónico

    # METODOS GETTERS (ACCEDER A ATRIBUTOS PRIVADOS)
    def get_voltaje(self):
        return self._voltaje

    def get_consumo_energetico(self):
        return self._consumo_energetico

# CLASE PRODUCTOALIMENTICIO QUE HEREDA DE PRODUCTO
class ProductoAlimenticio(Producto):
    def __init__(self, categoria, nombre_prod, precio, cantidad, fecha_vencimiento):
        super().__init__(categoria, nombre_prod, precio, cantidad)  # Herencia y uso de super() para inicializar atributos de la clase base
        self._fecha_vencimiento = fecha_vencimiento  # Atributo adicional (encapsulado) para la fecha de vencimiento del producto alimenticio

    # METODO GETTER (ACCEDER A ATRIBUTO PRIVADO)
    def get_fecha_vencimiento(self):
        return self._fecha_vencimiento

# CLASE INVENTARIO
class Inventario:
    def __init__(self):
        self.productos = []  # Atributo (encapsulado) para almacenar la lista de productos en el inventario

    def agregar_producto(self, producto):
        self.productos.append(producto)  # Método para agregar un producto a la lista de productos

    def buscar_producto(self, id):
        for producto in self.productos:
            if producto.get_id() == id:  # USO DE METODO GETTER PARA ACCEDER A ATRIBUTO PRIVADO (ID del producto)
                return producto
        return None

    def eliminar_producto(self, id):
        producto = self.buscar_producto(id)  # Usando otro método para buscar producto
        if producto:
            self.productos.remove(producto)  # Método para eliminar un producto de la lista
            print("/////Producto eliminado del inventario/////")
        else:
            print("El producto no existe")

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
            producto.get_id(), producto.get_categoria(), producto.get_nombre_prod(), producto.get_precio(), producto.get_cantidad()) for producto in productos)))
        print(tabla_inventario)  # Método para mostrar el inventario

# FUNCIÓN QUE MUESTRA UN MENÚ DE OPCIONES
def Menu():
    print("Elija una opción: \n1. Agregar producto \n2. Eliminar producto \n3. Buscar un producto \n4. Ver inventario completo \n5. Cerrar inventario")

#----------------------------------------------------------------------------#
################################# INSTANCIA  #################################
#----------------------------------------------------------------------------#

# CREACIÓN DE UNA INSTANCIA DE LA CLASE INVENTARIO

inventario = Inventario()

while True:
    Menu()
    opcion = int(input())
    if opcion == 1:
        print("Seleccione el tipo de producto: \n1. Producto Consumible \n2. Producto Electrónico")
        tipo_producto = int(input())

        if tipo_producto != 1 and tipo_producto != 2:
            print("Opción incorrecta")
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

            inventario.agregar_producto(producto)  # Uso del método para agregar un producto
            print(f"\n/////Producto agregado al inventario///// \nID nuevo producto: {producto.get_id()}\n")

    elif opcion == 2:
        print("Ingrese el ID del producto a eliminar:")
        id_eliminar = int(input())
        inventario.eliminar_producto(id_eliminar)  # Uso del método para eliminar un producto

    elif opcion == 3:
        print("Ingrese el ID del producto que desea buscar:")
        id_buscar = int(input())
        producto_encontrado = inventario.buscar_producto(id_buscar)  # Uso del método para buscar un producto
        if producto_encontrado:
            print(f"\n/////Producto encontrado///// \nID: {producto_encontrado.get_id()} \nCategoría: {producto_encontrado.get_categoria()} \nNombre: {producto_encontrado.get_nombre_prod()} \nPrecio: {producto_encontrado.get_precio()} \nCantidad: {producto_encontrado.get_cantidad()}")
            if isinstance(producto_encontrado, ProductoElectronico):
                print(f"Voltaje: {producto_encontrado.get_voltaje()} \nConsumo Energético: {producto_encontrado.get_consumo_energetico()}")
            elif isinstance(producto_encontrado, ProductoAlimenticio):
                print(f"Fecha de Vencimiento: {producto_encontrado.get_fecha_vencimiento()}\n")
        else:
            print(f"No se encontró un producto con el ID: {id_buscar}")

    elif opcion == 4:
        inventario.mostrar_inventario()  # Uso del método para mostrar el inventario
    elif opcion == 5:
        break
    else:
        print("Opción incorrecta. Por favor seleccione una opción válida.")
