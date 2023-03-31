from enum import Enum

class ParamType(Enum):
    OBJECT = 1
    RELATION = 2
    VARIABLE = 3

class Parameter():
    def __init__(self, value, param_type: ParamType):
        self.value = value
        self.param_type = param_type
