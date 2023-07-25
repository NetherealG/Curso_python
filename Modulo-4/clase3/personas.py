class Persona :
    def __init__(self, _nacionalidad, _edad, _sexo):
        self.nacionalidad = _nacionalidad
        self.edad = _edad
        self.sexo = _sexo

class Materias:
    def __init__(self, _asignatura, _Horas_asignatura ):
        self.asignatura = _asignatura
        self.Horas_asignatura = _Horas_asignatura
        
  
        
class Maestro(Persona, Materias):
    def __init__(self,_nacionalidad, _edad, _sexo, _asignatura, _Horas_asignatura):
         Persona.__init__(_nacionalidad, _edad, _sexo)
         Materias.__init__(self, _asignatura, _Horas_asignatura )
         
         
        
      
       
class Estudiante (Persona,Materias):
    def __init__(self,_nacionalidad, _edad, _sexo, _asignatura, _año_cursando, _Horas_asignatura):
         Persona.__init__(_nacionalidad, _edad, _sexo)
         Materias.__init__(self, _asignatura, _Horas_asignatura )
         self.año_cursando = _año_cursando
         
        
        
        
    
class Universitario (Estudiante,Materias):
    def __init__(self,_nacionalidad, _edad, _sexo, _asignatura, _año_cursando, _semestres_completos, _Horas_asignatura):
         Estudiante.__init__(self,_nacionalidad, _edad, _sexo, _asignatura, _año_cursando)
         Materias.__init__(self, _asignatura, _Horas_asignatura)
         self.semestres = _semestres_completos
         
        
    