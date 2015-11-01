#!/usr/bin/python
# -*- coding: utf-8 -*-
import copy

class TuringMachine(object):
    def __init__(self):
        self.memory=["",]
        self.memory_pointer=0
        self.current_state="q0"
        self.settings=[]
    
    def __str__(self):
        return "Memory:\n"+str(self.memory)+"\n\nMemory Pointer:\nM["+str(self.memory_pointer)+"]-->'"+str(self.memory[self.memory_pointer])+"'\n\nCurrent State:\n"+self.current_state

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


class ExecutionHandler(object):
    def __init__(self):
        self.step=0
        self.back_stack=[]
        self.current_machine=TuringMachine()
        self.next_stack=[]    

    def __init__(self, TuringMachine):
        self.step=0
        self.back_stack=[]
        self.current_machine=TuringMachine
        self.next_stack=[]    

    def __str__(self):
        return  "\n--------Step: "+str(self.step)+"--------\n"+str(self.current_machine) 

    def run_step(self):
        self.back_stack.append(copy.deepcopy(self.current_machine))
        if self.current_machine.execute():           
            self.next_stack=[]        
            self.step+=1
            return True
        self.back_stack.pop()
        return False

    def step_forward(self):
        if self.next_stack:
            self.back_stack.append(copy.deepcopy(self.current_machine))
            self.current_machine=self.next_stack.pop()
            self.step+=1
            return True
        return False

    def step_back(self):
        if self.back_stack:
            self.next_stack.append(copy.deepcopy(self.current_machine))
            self.current_machine=self.back_stack.pop()
            self.step-=1
            return True
        return False

    def execute(self):
        print self
        while self.run_step():
            print self

    def go_start(self):      
        print self
        while self.step_back():
            print self

    def go_end(self):      
        print self
        while self.step_forward():
            print self
