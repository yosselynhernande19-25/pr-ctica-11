import modulo1

radio = 5
area = modulo1.area_circulo(radio)
perimetro = modulo1.perimetro_circulo(radio)
print(f"Área del círculo con radio {radio}: {area}")
print(f"Perímetro del círculo con radio {radio}: {perimetro}")

ancho = 4
alto = 6
area = modulo1.area_rectangulo(ancho, alto)
perimetro = modulo1.perimetro_rectangulo(ancho, alto)
perimetro = modulo1.perimetro_rectangulo(ancho, alto)
print(f"Área del rectángulo de ancho {ancho} y alto {alto}: {area}")
print(f"Perímetro del rectángulo de ancho {ancho} y alto {alto}: {perimetro}")

base = 3
altura = 4
lado1 = 5
lado2 = 5
lado3 = 7
area = modulo1.area_triangulo(base, altura)
perimetro = modulo1.perimetro_triangulo(lado1, lado2, lado3)
print(f"Área del triángulo con base {base} y altura {altura}: {area}")
print(f"Perímetro del triángulo con lados {lado1}, {lado2} y {lado3}: {perimetro}")

