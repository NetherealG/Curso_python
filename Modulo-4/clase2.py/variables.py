class Alumno:
    semestre = 1
    asignaturas = ["Python", "Javascript","Base de datos"] 
    
    def __init__(self, _name):
        self.name = _name
        self.asignatura = ""
        
    def inscribir_asignatura(self, _asignatura):
        self.asignatura = _asignatura
    
    
alumno1 = Alumno("martin")
alumno2 = Alumno("roberto")
alumno3 = Alumno("nicolas")

print(f'alumno1: {alumno1.name} --- alumno2: {alumno2.name} --- alumno3: {alumno3.name}')
print(f'semestre alumno1 :{alumno1.semestre} --- semestre alumno2 :{alumno2.semestre} --- semestre alumno3 :{alumno3.semestre}')


alumno2.semestre = 2
print(f'semestre alumno1 :{alumno1.semestre} --- semestre alumno2 :{alumno2.semestre} --- semestre alumno3 :{alumno3.semestre}')

Alumno.semestre = 3
print(f'semestre alumno1 :{alumno1.semestre} --- semestre alumno2 :{alumno2.semestre} --- semestre alumno3 :{alumno3.semestre}')

