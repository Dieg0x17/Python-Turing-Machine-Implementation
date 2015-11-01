#!/usr/bin/python
# -*- coding: utf-8 -*-
from tm import TuringMachine, ExecutionHandler


# Configuración basica para un programa que multiplica por 2 un numero unario preseteado en memoria utilizando un simbolo auxiliar.
tm = TuringMachine()
# ( estado inicial, simbolo que reconoce, simbolo que deja en memoria, desplazamiento, estado final)
tm.settings=[
("q0",'1','0','L','q1'),    
("q1",'1','1','L','q1'),
("q1",'' ,'1','R','q2'),
("q2",'1','1','R','q2'),
("q2",'0','1','R','q0'),
]
tm.memory=['','1','1','']
tm.memory_pointer=1
tm.current_state="q0"

    
def ex1():
    """
        Complex execution example using the ExecutionHandler wrapper class
    """
    eh=ExecutionHandler(tm)
    eh.execute()

    eh.go_start()

    if eh.step_forward():
        print eh

    eh.go_end()

    if eh.step_back():
        print eh

def ex2():
    """
        Simple lineal execution
    """
    i=0
    while tm.execute():
        print "Step - "+str(i)
        print tm
        i+=1


ex1()
