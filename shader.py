from PIL import Image
from pylab import *
import numpy as np

def pixcolor(v):
	return (int(v[0]),int(v[1]),int(v[2]))



size = 512, 512

c = np.array([256,256,500])

o = np.array([256,256,0])

plano = 200

r = 300

k = np.array([255, 141, 0])

amb = np.array([85,47,0])

L = np.array([-1,-1,-0.5])

scene = Image.new('RGB', size, color = 'black')

for i in range(size[0]):
	for j in range(size[1]):
		sigma = np.array([i,j,plano] - o)
		coef = [np.linalg.norm(sigma)*np.linalg.norm(sigma),2*np.dot(sigma,o-c),np.linalg.norm(o-c)*np.linalg.norm(o-c) - r*r]
		raiz = np.roots(coef)[1]
		if np.isreal(raiz) and raiz >= 0:
			normal = (raiz*sigma + o - c)/np.linalg.norm(raiz*sigma + o - c)
			L = L/np.linalg.norm(L)
			cos = np.dot(normal,L)
			if cos < 0:
				cos = 0
			cor = cos*k + amb
			scene.putpixel((i,j),pixcolor(cor))


imshow(scene)
show()
