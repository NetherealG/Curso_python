from datetime import datetime

fecha = datetime.now()
cant_entradas_vendidas = 0
atracciones_disponibles = ['Montaña rusa', 'Tobogan de agua', 'Autos chocadores']
cantidad_veces_atraccion_utilizada = {'Montaña rusa': 0, 'Tobogan de agua': 0, 'Autos chocadores': 0}
capacidad_maxima_atraccion = {'Montaña rusa': 40, 'Tobogan de agua': 70, 'Autos chocadores': 70}
precio_entradas = 12000.0
ingresos_totales = 0.0

def vender_entradas(cantidad):
    global cant_entradas_vendidas, ingresos_totales
    cant_entradas_vendidas += cantidad
    ingresos_totales += cantidad * precio_entradas

def utilizar_atraccion(atraccion, cantidad):
    global cantidad_veces_atraccion_utilizada, ingresos_totales
    cantidad_veces_atraccion_utilizada[atraccion] += cantidad
    ingresos_totales += cantidad * precio_entradas

# Ejemplo de uso: registrar la venta de 50 entradas y el uso de la atracción "Montaña Rusa" 20 veces
vender_entradas(50)
utilizar_atraccion("Montaña rusa", 20)

# Mostrar los valores actuales de los atributos
print("Fecha:", fecha)
print("Cantidad de entradas vendidas:", cant_entradas_vendidas)
print("Atracciones disponibles:", atracciones_disponibles)
print("Cantidad de veces que se ha utilizado cada atracción:", cantidad_veces_atraccion_utilizada)
print("Capacidad máxima de cada atracción:", capacidad_maxima_atraccion)
print("Precio de las entradas:", precio_entradas)
print("Ingresos totales:", ingresos_totales)