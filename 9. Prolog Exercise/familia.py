#Gabriel Esteban Castillo Ramirez - 20171020021
from pyswip import Prolog
prolog = Prolog()
prolog.consult('familia.pl')

for result in prolog.query("padrede(X,Y)"):
	print result['X'] + " padre de " + result['Y']

print
for result in prolog.query("hijode(X,Y)"):
	print result['X'] + " hijo de " + result['Y']

print
for result in prolog.query("abuelode(X,Y)"):
	print result['X'] + " abuelo de " + result['Y']
	
print
for result in prolog.query("hermanode(X,Y)"):
	print result['X'] + " hermano de " + result['Y']

print
for result in prolog.query("tiode(X,Y)"):
	print result['X'] + " tio de " + result['Y']

print
for result in prolog.query("sobrinode(X,Y)"):
	print result['X'] + " sobrino de " + result['Y']

print
for result in prolog.query("primode(X,Y)"):
	print result['X'] + " primo de " + result['Y']

print
for result in prolog.query("bisabuelode(X,Y)"):
	print result['X'] + " bisabuelo de " + result['Y']

print
for result in prolog.query("bisnietode(X,Y)"):
	print result['X'] + " bisnieto de " + result['Y']

print
for result in prolog.query("casadocon(X,Y)"):
	print result['X'] + " casado con " + result['Y']

print
for result in prolog.query("esfeliz(X)"):
	print result['X'] + " es feliz" 
	
