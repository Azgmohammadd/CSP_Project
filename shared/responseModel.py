from typing import Any

class ResponseModel():
    result: Any
    hasError: bool
    message: str
    
    def __init__(self, response: Any, hasError: bool, message: str):
        self.result = response
        self.hasError = hasError
        self.message = message
        
    
    def __str__(self) -> str:
        return f"result: {self.result}, hasError: {self.hasError}, message: {self.message}"