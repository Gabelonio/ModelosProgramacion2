%Nucleo.
padrede('pedro','gabriel').
padrede('pedro','daniel').
padrede('cristina','gabriel').
padrede('cristina','daniel').

%Abuelos.
padrede('leonel','pedro').
padrede('otilia','pedro').
padrede('emeteria','cristina').

%Bisabuela.
padrede('anarosa','emeteria').

%Tios.
padrede('emeteria','rosa').
padrede('emeteria','clemencia').
padrede('emeteria','amparo').
padrede('emeteria','alfonso').
padrede('emeteria','gonzalo').

padrede('leonel','alejandro').
padrede('leonel','rosember').
padrede('leonel','nelson').

%Primos.
padrede('rosa','sara').
padrede('wilson','sara').

padrede('clemencia','alejo').
padrede('clemencia','jhon').
padrede('clemencia','jeison').
padrede('manuel','alejo').
padrede('manuel','jhon').
padrede('manuel','jeison').

padrede('amparo','july').
padrede('amparo','mariana').
padrede('hernan','july').
padrede('hernan','mariana').

padrede('gonzalo','camilo').
padrede('gonzalo','catalina').
padrede('gonzalo','andres').
padrede('ana','camilo').
padrede('ana','catalina').
padrede('ana','andres').

padrede('alfonso','adriana').
padrede('alfonso','federico').

padrede('alejandro','wendy').
padrede('alejandro','mari').
padrede('catherine','wendy').
padrede('catherine','mari').


hijode(A,B) :- padrede(B,A).

abuelode(A,B) :- padrede(A,C), padrede(C,B).
	
nietode(A,B) :- abuelode(B,A).

hermanode(A,B) :- padrede(C,A), padrede(C,B), A \== B.

tiode(A,B) :- hermanode(A,C), padrede(C,B).

sobrinode(A,B) :- tiode(B,A).

primode(A,B) :- tiode(A,C), padrede(C,B).

bisabuelode(A,B) :- abuelode(A,C), padrede(C,B).

bisnietode(A,B) :- bisabuelode(B,A).

casadocon(A,B) :- padrede(A,C), padrede(B,C), A \== B.

esfeliz(A) :- casadocon(A,C).
