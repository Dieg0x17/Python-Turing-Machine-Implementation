#!/usr/bin/python
# -*- coding: utf-8 -*-

class TuringMachine(object):

    def __init__(self):
        self.memory=["",]
        self.memory_pointer=0
        self.current_state="q0"
        self.settings=[]  
    
    def preload_memory(self, l):
        self.memory=l
    
    def set_current_state(self, state):
        self.current_state=state

    def resize_memory(self):
        if self.memory_pointer < 0:
            self.memory.insert(0,"") 
            self.memory_pointer+=1

        if self.memory_pointer > len(self.memory)-1:
            self.memory.append("")

    def load_settings(self, f):
        """
            Abre un archivo de configuración que contiene
            -el estado de la memoria inicial.
            -la función de transicción.
            -la posición inicial del puntero.
        """
        pass # TODO

    def execute(self):
        """
            Ejecuta un ciclo de la maquina de turing
            devuelve True si hay ejecución y false si no hay
        """
        for rule in self.settings:
            if rule[0] == self.current_state:
                if rule[1] == self.memory[self.memory_pointer]:
                    self.memory[self.memory_pointer]=rule[2]
                    if rule[3] == 'L':
                        self.memory_pointer-=1
                    elif rule[3] == 'R':
                        self.memory_pointer+=1
                    self.resize_memory()
                    self.current_state=rule[4]
                    return True
        return False


    def full_exec(self):
        i=0
        while self.execute():
            print "############ step "+str(i)
            print "Memory:"
            print self.memory
            print ""
            print "Memory Pointer:"
            print (self.memory_pointer, self.memory[self.memory_pointer])
            print ""
            print "Current State:"
            print self.current_state
            print ""
            i+=1
            
 

def main():
    tm = TuringMachine()

    # Configuración basica para un programa que multiplica por 2 un numero unario preseteado en memoria utilizando un simbolo auxiliar.

    tm.settings=[
    # ( estado inicial, simbolo que reconoce, simbolo que deja en memoria, desplazamiento, estado final)
    ("q0",'1','0','L','q1'),    
    ("q1",'1','1','L','q1'),
    ("q1",'' ,'1','R','q2'),
    ("q2",'1','1','R','q2'),
    ("q2",'0','1','R','q0'),
    ]
    tm.preload_memory(['','1','1',''])
    tm.set_current_state("q0")
    tm.memory_pointer=1

    tm.full_exec()

main()
