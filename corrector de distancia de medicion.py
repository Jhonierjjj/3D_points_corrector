import math
import numpy as np

def mag (vector):
    
    return math.sqrt(sum(pow(v,2) for v in vector)) 

def corrector (vector,m,g):
    vector = np.float64([v+(v*g/m) for v in vector])
    return vector 
 
nube = np.loadtxt('nube a corregir.txt',dtype=float, delimiter=input('En el txt de entrada, ¿que elemento separa los datos?'))
print('Espere')
gap = float(input("Introduzca la distancia de corrección en mm, siendo negativo reducir distancia respecto del tracker y positivo aumentarla: "))

print('Espere')

for i in range(0,nube.shape[0]):

    v = np.float64(nube[i])
    magnitude = mag(v)
    nube[i] = corrector(v,magnitude,gap)


np.savetxt('nube corregida.txt',nube,fmt='%.6f')

print('Listo')