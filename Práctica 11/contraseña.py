import os 
from time import sleep
import generador_contraseña as mc

contraseña = mc.generador_contraseña(14)
print(contraseña)