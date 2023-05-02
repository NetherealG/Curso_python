class Droid:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name (self, name:str) -> None:
        self._name = name
        
Roberto = Droid("Roberto")

print(Roberto.name)

class Artefacts:
    def __init__(self, _Mythical , _Rare , _legendary):
        self.__Mythical = _Mythical
        self.__Rare = _Rare
        self.__Legendary = _legendary
    
    @property
    def _Mythical(self) -> str:
        return self.__Mythical
    
    @_Mythical.setter
    def _Mythical (self, name:str) -> None:
        self.__Mythical = name
        
    

