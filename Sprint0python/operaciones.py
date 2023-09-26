# Suma de dous valores
def suma(a, b):
    return  int(a) + int(b)

# Resta de dous valores
def resta(a, b):
    return int(a) - int(b)

# Multiplicación de dous valores
def multiplicacion(a, b):
    return int(a) * int(b)

# Division de dous valores
def division(a, b):
    if int(b) == 0:
        return "Dividir entre 0, non e posible"
    else:
        return int(a) / int(b)

