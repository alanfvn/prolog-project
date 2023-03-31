from pickle import NONE


SYNONYMS = {
    "abuelo": [
        "abuelastro",
        "abuelazo"
        "abuelillo",
        "abuelito",
        "anciano",
        "viejito",
    ],
    "abuela": [
        "abuelita",
        "anciana",
        "viejita",
    ],
    "padre": [
        "jefe",
        "papa",
        "papi",
        "papito",
        "patriarca",
        "progenitor",
        "viejo",
    ],
    "madre": [
        "jefa",
        "madrecita",
        "mama",
        "mami",
        "mamita",
        "progenitora",
    ],
    "hijo": [
        "cachorro",
        "descendiente",
        "heredero"
        "nino",
        "sucesor",
    ],
    "hija": [
        "cachorra",
        "heredera",
        "infanta",
        "nina",
        "sucesora",
    ],
    "hermano": [
        "hermanastro",
        "brother"

    ],
    "hermana": [
        "hermanastra",
        "sister"
    ],
    "nieto": [],
    "nieta": [],
}

OBJECTS = [
    "alan",
    "argelio",
    "david",
    "ericka",
    "florinda",
    "humberto",
    "jackeline",
    "olga",
]

VARIABLES = [
    "quien",
]


def find_relation(word):
    if word in SYNONYMS:
        return word
    # word is not in the dictionary search inside the synonyms list
    for key, value in SYNONYMS.items():
        find = next((syn for syn in value if syn == word), None)
        if find is not None:
            return key

    return None 

def find_vars(variable):
    val = next((var for var in VARIABLES if var == variable), None)
    return val

def find_object(obj):
    val = next((ob for ob in OBJECTS if ob == obj), None)
    return val


def search_parameters(sentence):
    words = sentence.split()

    relations, objects, variables = [], [], []

    for word in words:
        # find relations
        rel = find_relation(word)
        if rel is not None:
            relations.append(rel)
            continue

        # find objects
        obj = find_object(word)
        if obj is not None:
            objects.append(obj)
            continue

        # find vars
        var = find_vars(word)
        if var is not None:
            variables.append(var)
            continue

    return {
        "relations": relations,
        "objects": objects,
        "variables": variables
    }
