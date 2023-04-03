from typing import List
from models.parameter import Parameter, ParamType
from data.values import RELATIONS, VARIABLES, OBJECTS

def find_values(word):
    """
    returns a Parameter or None
    """
    # check for relations
    if word in RELATIONS:
        return Parameter(word, ParamType.RELATION)

    # word is not in the dictionary search inside the synonyms list
    for key, value in RELATIONS.items():
        find = next((syn for syn in value if syn == word), None)
        if find is not None:
            return Parameter(key, ParamType.RELATION)

    # check for variables
    variable = next((var for var in VARIABLES if var == word), None)
    if variable is not None:
        return Parameter(variable, ParamType.VARIABLE)

    # check for objects
    obj = next((ob for ob in OBJECTS if ob == word), None)
    if obj is not None:
        return Parameter(obj, ParamType.OBJECT)

    # nothing has been found
    return None


def check_sentence(params: List[Parameter]):
    """
    Rules for a good sentence:
    - 3 parameters
    - relation must be in the middle
    - (1 object and 1 variable) or (1 variable and 1 object )
    - (2 variables) or (2 objects)
    """
    if len(params) != 3:
        return False

    patterns = [
        [ParamType.OBJECT, ParamType.RELATION, ParamType.OBJECT],
        [ParamType.VARIABLE, ParamType.RELATION, ParamType.VARIABLE],
        [ParamType.OBJECT, ParamType.RELATION, ParamType.VARIABLE],
        [ParamType.VARIABLE, ParamType.RELATION, ParamType.OBJECT]
    ]
    # extract all paramter types
    ptypes = [param.param_type for param in params]
    # check if all paramters match a defined pattern
    return ptypes in patterns


def search_parameters(sentence):
    words = sentence.split()
    params = []

    for word in words:
        param = find_values(word)
        if param is not None:
            params.append(param)
            continue

    return params

def construct_query(params: List[Parameter]):
    rel = params[1].value
    val1 = params[0]
    val2 = params[2]

    obj1 = val1.value if val1.param_type == ParamType.OBJECT else 'X' 
    obj2 = val2.value if val2.param_type == ParamType.OBJECT else 'Y'

    return {
        "relation": rel,
        "f_parameter": obj1,
        "s_parameter": obj2,
    }
