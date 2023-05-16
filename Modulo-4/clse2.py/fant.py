class Taza:
    sizes = {
        small: "pequeño",
        medium: "mediano",
        large: "grande"
    }
    def __init__(self) :
        self.size = sizes["small"]
        
class Maquina:
    type_coffe = {
        cof0: "expreso",
        cof1: "capuccino",
        cof2: "mokaccino",
        cof3: "americano"    
    }
    

    def __init__(self) :
        self.tipo_cafe =type_coffe["cof0"]
        self.cant_agua = 40,
        self.cant_cafe = 10
class Cafe:
    typegrano = {
        grano1 : "arabica",
        grano2 : "robusta",
        grano3 : "liberica"
        
    }
    def __init__(self) :
        self.tipograno = typegrano["grano1"]
class Leche:
    typemilk = {
        milk1 : "entera",
        milk2 : "semidescremada",
        milk3 : "descremada",
        milk3 : "sin lactosa",
        milk3 : "soja"   
    }
    def __init__(self) :
        self.tipograno = typemilk["milk1"]