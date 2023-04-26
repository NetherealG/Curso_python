def calificacion():
  na = float(input ("numero1: "))
  nb = float(input ("numero2: "))
  nc = float(input ("numero3: "))

  x = promedio (na, nb, nc)

  if x >= 0 or x <=2:
       print("calificación: D")
  if x >= 2.1 or x <=5 :
       print("calificación: C")
  if x >= 5.1 or x <=6:
       print("calificación: B")
  if x >= 6.1 or x <=7:
      print("calificación: A")

def promedio (a, b, c):
   x = (a + b + c)/3
   return x
calificacion()
