
def suma(a, b):
    return  int(a) + int(b)

def resta(a, b):
    return int(a) - int(b)


def multiplicacion(a, b):
    return int(a) * int(b)

def division(a, b):
    if int(b) == 0:
        return "Wrong. Division by 0 is not possible"
    else:
        return int(a) / int(b)

