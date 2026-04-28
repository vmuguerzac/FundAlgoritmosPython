def CalcularIMC(peso, altura):
    imc = 0.0
    # validar datos de entrada
    valido = ValidarEntrada(peso, altura)
    if valido  == True:
        # Proceso
        imc = peso / altura ** 2
    else:
        print("Datos de entrada no valido")
    return imc

def ValidarEntrada(peso, altura):
    valido = False
    if peso <= 400 and peso >= 5:
        if altura <= 2.5 and altura >= 0.6:
          valido = True
        else:
            print("Altura inválida")
            valido = False
    else:
        print("Peso invalido")
        valido = False
    return valido  

# Programa que calcula el IMC
# Declaracion y obtencion de datos
peso = float(input("Ingrese su peso (Kg): "))
altura = float(input("Ingrese su altura (m): "))
imc = CalcularIMC(peso, altura)
if imc > 0:
    # Mostrar informacion
    print("Su imc es: ", imc)

