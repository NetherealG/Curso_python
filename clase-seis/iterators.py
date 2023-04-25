words = "esto es una cadena de texto"

word = ''
for letter in words: 
    if letter != ' ':
        word += letter
    else:
        print(word)
        word = ''
        
for letter in words: 
 if letter != ' ':
     print (letter)
 else:
     break
animal_list = ['gato', 'perro', 'pajaro', 'ardilla']
for animal in animal_list:
    print(animal)
    
list1 = range(2,3)
print(list1)

for number_in in range(1,10):
    print(number_in)

print("\n--------tablas de multiplicar---------\n")
for num_tabla in range(1, 11):
    for num_mul in range(1, 11):
        result = num_tabla * num_mul
        print(f'{num_tabla} x {num_mul} ={result}')
print("\n-----------------\n")

print("\n-------arreglos bidimencionales----------\n")

double_list [[1, 2, 3][4, 6, 7]]




    