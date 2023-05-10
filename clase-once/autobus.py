#se necesita realizar un programa basado en clases que permita automatizar el torniquete (control de acceso)
#de una micro, de la siguiente manera

 #   1 Las personas que aboradan la micro son, mujeres, hombres, niños y aduto mayor, de los cuales los niños no pagan y lso adultos mayores pagan la tarifa
  #    el 50%
    
   # 2 el cobro actual de la micro es de 730 pesos

    #3 por lo que necesitamos un reporte de operacion por dia donde, por micro (cada micro se reguistra por patente), se listen los tipos de usuario y la cantidad total recaudad por 
#      cada, anexar a este reporte el total por dia

    #4. seria interesante que apart6e del reporte anterior que estotal, tener uno filtrado por dia y otro filtrado por persona

class Usuario:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo

class Micro:
    def __init__(self, patente, precio):
        self.patente = patente
        self.precio = precio
        self.usuarios = []
        self.montos = {"mujer": 0, "hombre": 0, "niño": 0, "adulto mayor": 0}

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
        if usuario.tipo == "niño":
            # Niños no pagan
            pass
        elif usuario.tipo == "adulto mayor":
            # Descuento del 50% para adultos mayores
            monto = self.precio / 2
            self.montos["adulto mayor"] += monto
        else:
            self.montos[usuario.tipo] += self.precio

    def reporte_total(self):
        print("Reporte total para la micro de patente", self.patente)
        for tipo, monto in self.montos.items():
            print("Tipo de usuario:", tipo)
            print("Cantidad recaudada:", monto)

    def reporte_filtrado_dia(self, dia):
        total_dia = 0
        print("Reporte para la micro de patente", self.patente, "en el día", dia)
        for usuario in self.usuarios:
            if usuario.dia == dia:
                if usuario.tipo == "niño":
                    # Niños no pagan
                    pass
                elif usuario.tipo == "adulto mayor":
                    # Descuento del 50% para adultos mayores
                    monto = self.precio / 2
                    total_dia += monto
                else:
                    total_dia += self.precio
        print("Total recaudado en el día:", total_dia)

    def reporte_filtrado_persona(self, nombre):
        total_persona = 0
        print("Reporte para la persona", nombre)
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                if usuario.tipo == "niño":
                    # Niños no pagan
                    pass
                elif usuario.tipo == "adulto mayor":
                    # Descuento del 50% para adultos mayores
                    monto = self.precio / 2
                    total_persona += monto
                else:
                    total_persona += self.precio
        print("Total recaudado por la persona:", total_persona)

micro = Micro("AB1234", 730)

usuario1 = Usuario("Juan", 35, "hombre")
micro.agregar_usuario(usuario1)

usuario2 = Usuario("María", 25, "mujer")
micro.agregar_usuario(usuario2)

usuario3 = Usuario("Pedro", 8, "niño")
micro.agregar_usuario(usuario3)

usuario4 = Usuario("Carmen", 70, "adulto mayor")
micro.agregar_usuario(usuario4)

micro.reporte_total()
