from typing import Any

class ResponseModel():
    __result: Any
    __hasError: bool
    __message: str
    
    def __init__(self, response: Any, hasError: bool, message: str):
        self.__result = response
        self.__hasError = hasError
        self.__message = message
        
    
    def __str__(self) -> str:
        return f"result: {self.__result}, hasError: {self.__hasError}, message: {self.__message}"