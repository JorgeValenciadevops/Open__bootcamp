"PYTHON IS  STRONGLY TYPED AND DYNAMYC"
"MUTABLES AND IMMUTABLE "
"TUPLAS AND DITIONARY"
"IN A SET {} THERE CAN'T BE EQUAL  ELEMENTS"
"METHODOS TO STRING"
"OPERATORS"
"CONDITIONALS "
"IF, ELIF  ELSE WHILE" "BREAK, CONTINUE"
"FOR WITH ELSE "
"MATCH"
"KWARGS "


def sumador(**kwargs):
    # Operador ternario
    # Operador ternario
    inicial = kwargs['inicial'] if 'initial' in kwargs else 0
    final = kwargs['final'] if 'final' in kwargs else 0  # Operador ternario
    resultado = 0

    for x in range(inicial, final+1):
        resultado += x

    return resultado


sumador(inicial=10, final=15)
"FUNCIONES LAMBDA"
