class CustomHttpException(Exception):
    def __init__(self, _code=500, _message= "Internal Server Error"):
        self.code = _code
        self.message = _message

try:
    raise CustomHttpException()
except Exception as error:
    print(error.code)
    print(error.message)

try:
    raise CustomHttpException(400, "Bad Request")
except Exception as error:
    print(error.code)
    print(error.message)