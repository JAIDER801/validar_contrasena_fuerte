#27. Validar contraseña fuerte
def elementos_vacios(elementos):
    if not elementos:
        print("\nInvalido. La entrada de los elementos no puede estar vacia.")
        exit()

def continuar_programa():
    continuar = input("\n¿Desea continuar con el programa?, (s,n): ").strip().lower()
    if continuar in ("s", "si"):
        return True
    else:
        print("\nEl programa a terminado.")
        return False

def verificar_contraseña(contraseña):
    if not 6 <= len(contraseña) <= 12:
        return False

    numeros = 0
    mayusculas = 0
    minusculas = 0
    caracteres_especiales = 0

    for caracter in contraseña:
        if caracter.isspace():
            return False
        elif caracter.isdigit():
            numeros += 1
        elif caracter.isupper():
            mayusculas += 1
        elif caracter.islower():
            minusculas += 1
        elif caracter in "#$!%&@/":
            caracteres_especiales += 1

    return numeros >= 2 and mayusculas != 0 and minusculas > 3 and caracteres_especiales != 0

while True:
    print("\n--- Reglas de Validación ---")
    print("1. Tener al menos un número")
    print("2. Tener al menos una letra mayúscula")
    print("3. Tener al menos una letra minúscula")
    print("4. Debe contener al menos un carácter especial ($, @, #, %, &, !, /)")
    print("5. Debe contener entre 6 y 20 caracteres de longitud")

    contraseña_ingresada = input("\nIngrese su contraseña, por favor: ").strip()

    elementos_vacios(contraseña_ingresada)

    print(f"\n{verificar_contraseña(contraseña_ingresada)}")

    if not continuar_programa():
        break
