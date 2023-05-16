requisitos = {
    "Titulo": "Requerido",
    "Notas": "Requerido",
    "Foto": "opcional"
}

print (requisitos)


print (f'Las notas son de tipo:{requisitos["Notas"]}')
requisitos["Notas"] = "Optional"

print (f'Las notas son de tipo:{requisitos["Notas"]}')

print (f'Las fotos son de tipo:{requisitos["Foto"]}')
requisitos["Foto"] = "Ya ingresada"
print (f'Las fotos son de tipo:{requisitos["Foto"]}')


