import random

def generador_contraseña(longitud):
  caracteres = "Ejosbcnmmujm43278OPGTJLZ"
  contraseña = ""
  for _ in range(longitud):
    contraseña += caracteres[random.randint(0, len(caracteres) - 1)]
  return contraseña
