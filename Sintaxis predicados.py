## ejemplo de sintaxis para definir predicados con distintas aridades
## Referencia: Stackoverflow. "Call prolog predicate from python". Recuperado de: 
## http://stackoverflow.com/questions/6103461/call-prolog-predicate-from-python

## Open book Project. ""http://www.openbookproject.net/py4fun/prolog/prolog2.html

rD( [], Ans, Ans ).
rD( [X|Xs], Ans, Acc ) :-
    member( X, Acc ),
    rD( Xs, Ans, Acc ), !.
rD( [X|Xs], Ans, Acc ) :-
    \+member( X, Acc ),
    append( Acc, [X], AccNew ),
    rD( Xs, Ans, AccNew ), !.
