
dividendo = 100
while True:
    try:
        edad = int(input("Introduce tu edad: "))
        result = dividendo / edad
        break
    except ValueError as error:
        print(type(error))
        print(error.args)
        print(error)
    except ZeroDivisionError as error:
        print(type(error))
        print(error.args)
        print(error)
        
 
   