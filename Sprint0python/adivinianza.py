print("Adivinanza: Que es verde por fuera, pero rojo por dentro?")
print("A: Carlos.")
print("B: Sandia (Esta es la correcta).")
print("C: Melon (Es lo que eres si eligues la opción A o C.)")
respuesta = input("Eligue la opcion correcta.").lower()
if respuesta == "a":
    print("Incorrecto. Creo que ya se lo que eres.")
elif respuesta == "b":
    print("Correcto, era facil verdad?!")
elif respuesta == "c":
    print("Incorrecto. Has leido las respuesta?")
else:
    print("Si das un valor diferente a A,B o C. Obviamente no esperes un buen resultado.")
