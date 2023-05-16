class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre


class Cliente:
    def __init__(self, nombre, direccion, email):
        self.nombre = nombre
        self.direccion = direccion
        self.email = email


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class CarritoDeCompras:
    def __init__(self, cliente):
        self.cliente = cliente
        self.items = []

    def agregar_producto(self, producto):
        self.items.append(producto)

    def eliminar_producto(self, producto):
        self.items.remove(producto)

    def calcular_total(self):
        total = 0
        for item in self.items:
            total += item.precio
        return total


class Envio:
    def __init__(self, direccion):
        self.direccion = direccion

    def generar_etiqueta(self):
        # Lógica para generar la etiqueta de envío
        print(f"Se generó la etiqueta de envío para la dirección: {self.direccion}.")


class Pago:
    def __init__(self, total):
        self.total = total

    def procesar_pago(self):
        # Lógica para procesar el pago a través del proveedor de pagos
        print(f"El pago de ${self.total} se ha procesado correctamente.")


class Factura:
    def __init__(self, cliente, carrito, direccion_envio):
        self.cliente = cliente
        self.carrito = carrito
        self.direccion_envio = direccion_envio

    def generar_factura(self):
        # Lógica para generar la factura en formato PDF o HTML
        print("Se generó la factura correctamente.")


class EnvioConFactura(Tienda, Factura, Envio):
    def __init__(self, tienda, cliente, carrito, direccion_envio):
        Tienda.__init__(self, tienda)
        Factura.__init__(self, cliente, carrito, direccion_envio)
        Envio.__init__(self, direccion_envio)


# Ejemplo de uso
tienda = Tienda("Mi Tienda")

cliente = Cliente("Juan Pérez", "Calle Principal", "juan@example.com")

producto1 = Producto("Camisa", 25)
producto2 = Producto("Pantalón", 40)
producto3 = Producto("Zapatos", 50)

carrito = CarritoDeCompras(cliente)
carrito.agregar_producto(producto1)
carrito.agregar_producto(producto2)
carrito.agregar_producto(producto3)

total_a_pagar = carrito.calcular_total()

direccion_envio = "Calle Principal, Ciudad"

envio_con_factura = EnvioConFactura(tienda.nombre, cliente, carrito, direccion_envio)
envio_con_factura.generar_etiqueta()
envio_con_factura.generar_factura()

pago = Pago(total_a_pagar)
pago.procesar_pago()
