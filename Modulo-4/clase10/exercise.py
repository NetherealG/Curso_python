class Cine:
    def __init__(self, nombre, rut, direccion):
        self.nombre = nombre
        self.rut = rut
        self.direccion = direccion
        self.salas = []
        self.cartelera = {}

    def agregar_sala(self, sala):
        self.salas.append(sala)

    def agregar_pelicula(self, fecha, pelicula, horarios, sala):
        if fecha not in self.cartelera:
            self.cartelera[fecha] = {}
        if pelicula not in self.cartelera[fecha]:
            self.cartelera[fecha][pelicula] = {}
        self.cartelera[fecha][pelicula][horarios] = sala

    def vender_boleto(self, fecha, pelicula, horario, tipo_entrada, asiento):
        if fecha in self.cartelera and pelicula in self.cartelera[fecha] and horario in self.cartelera[fecha][pelicula]:
            sala = self.cartelera[fecha][pelicula][horario]
            if sala.verificar_disponibilidad(asiento):
                sala.vender_boleto(tipo_entrada, asiento)
                return True
        return False

    def reporte_entradas_dia(self, fecha):
        if fecha in self.cartelera:
            total_entradas = 0
            for pelicula in self.cartelera[fecha]:
                for horario in self.cartelera[fecha][pelicula]:
                    sala = self.cartelera[fecha][pelicula][horario]
                    total_entradas += sala.entradas_vendidas()
            return total_entradas
        return 0

    def reporte_entradas_funcion(self, fecha, pelicula, horario):
        if fecha in self.cartelera and pelicula in self.cartelera[fecha] and horario in self.cartelera[fecha][pelicula]:
            sala = self.cartelera[fecha][pelicula][horario]
            return sala.entradas_vendidas()
        return 0

    def reporte_entradas_pelicula(self, pelicula):
        total_entradas = 0
        for fecha in self.cartelera:
            if pelicula in self.cartelera[fecha]:
                for horario in self.cartelera[fecha][pelicula]:
                    sala = self.cartelera[fecha][pelicula][horario]
                    total_entradas += sala.entradas_vendidas()
        return total_entradas

    def reporte_entradas_completo(self):
        reporte = {}
        for fecha in self.cartelera:
            reporte[fecha] = {}
            for pelicula in self.cartelera[fecha]:
                reporte[fecha][pelicula] = {}
                for horario in self.cartelera[fecha][pelicula]:
                    sala = self.cartelera[fecha][pelicula][horario]
                    reporte[fecha][pelicula][horario] = sala.entradas_vendidas()
        return reporte


class Sala:
    def __init__(self, numero_sala, capacidad):
        self.numero_sala = numero_sala
        self.capacidad = capacidad
        self.asientos_disponibles = capacidad
        self.entradas = {'normal': 0, 'vip': 0}

    def verificar_disponibilidad(self, asiento):
        if asiento <= self.capacidad and asiento > 0 and self.asientos_disponibles > 0:
            return True
        return False

    def vender_boleto(self, tipo_entrada, asiento):
        self.asientos_disponibles -= 1
        self.entradas[tipo_entrada] += 1

    def entradas_vendidas(self):
        return sum(self.entradas.values())


# Ejemplo de uso
cine = Cine("Cine Ejemplo", "12345678-9", "Dirección Ejemplo")

sala1 = Sala(1, 50)
sala2 = Sala(2, 80)

cine.agregar_sala(sala1)
cine.agregar_sala(sala2)

cine.agregar_pelicula("2023-05-21", "Avengers: Endgame", "18:00", sala1)
cine.agregar_pelicula("2023-05-21", "Spider-Man: Homecoming", "20:30", sala2)

cine.vender_boleto("2023-05-21", "Avengers: Endgame", "18:00", "normal", 10)
cine.vender_boleto("2023-05-21", "Spider-Man: Homecoming", "20:30", "vip", 5)

print("Total de entradas vendidas el día 2023-05-21:", cine.reporte_entradas_dia("2023-05-21"))
print("Entradas vendidas para la función Spider-Man: Homecoming - 20:30:", cine.reporte_entradas_funcion("2023-05-21", "Spider-Man: Homecoming", "20:30"))
print("Total de entradas vendidas para la película Avengers: Endgame:", cine.reporte_entradas_pelicula("Avengers: Endgame"))
print("Reporte completo de entradas vendidas:")
print(cine.reporte_entradas_completo())
