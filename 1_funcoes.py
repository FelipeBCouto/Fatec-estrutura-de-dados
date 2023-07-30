from math import pi

def calcular_area(base,altura,tipo):
    if tipo == "R": #retângulo
        return base * altura
    elif tipo == "T": #triângulo
        return base * altura / 2
    elif tipo == "E" or "C": #elipse ou círculo
        return (base / 2) * (altura / 2) * pi
    else:
        return None
    
print("Área retângulo 10x25: ",calcular_area(10,25,"R"))

base = int(input("Informe o valor da base: "))
altura = int(input("Informe o valor da altura: "))
tipo = input("Informe o tipo de forma geométrica, lembrando que:\na) R = retângulo\nb) T = triângulo\nc) E = elipse\nd) C = círculo\n")

if tipo == "R":
    print(f"A área do retângulo {base}x{altura} = ",calcular_area(base,altura,tipo))
elif tipo == "T":
    print(f"A área do triângulo {base}x{altura} = ",calcular_area(base,altura,tipo))
elif tipo == "E":
    print(f"A área do elipse {base}x{altura} = ",calcular_area(base,altura,tipo))
elif tipo == "C":
    print(f"A área do círculo {base}x{altura} = ",calcular_area(base,altura,tipo))
else:
    print("Tipo inválido.")