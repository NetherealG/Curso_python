class NewError(Exception):
    def __init__(self, *args):
        self.value = args
        
try: 
    raise NewError(1, 3, "casa", [0, 922])
except Exception as error:
    print(error.args)