#!/usr/bin/python
# -*- coding: utf-8 -*-
# copyrigth 2015 Diego Rasero de la Fuente, License: GNU GPL V2

#from tm import * # repositorio oficial https://github.com/Dieg0x17/Python-Turing-Machine-Implementation
import time
import os

class TuringMachine(object):
    def __init__(self):
        self.memory=["",]
        self.memory_pointer=0
        self.current_state="q0"
        self.settings=[]
    
    def __str__(self):
        return "\n"+str("".join(self.memory))+"\n"+str((self.memory_pointer-1)*' ')+"^\n"+str((self.memory_pointer-1)*' ')+str(self.current_state)+"\n"

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

# simulacion de una maquina universal de turing
m=TuringMachine() # se crea instancia de MT

# - simbolo de inicio de informacion
# = separador de registros
modulo_localizador = [
    # q0
    ("q0", '0','0','L',"q0"),
    ("q0", '1','1','L',"q0"),
    ("q0", 'A','A','L',"q0"),
    ("q0", 'B','B','L',"q0"),
    ("q0", '=','=','L',"q0"),
    ("q0", '-','-','R',"q1"),


    # q1
    ("q1", 'A','A','R',"q1"),
    ("q1", 'B','B','R',"q1"),
    ("q1", '0','A','R',"q2"),
    ("q1", '1','B','R',"q3"),
    ("q1", '=','=','R',"q9"),
    
    # q2
    ("q2", '0','0','R',"q2"),
    ("q2", '1','1','R',"q2"),
    ("q2", '=','=','R',"q4"),

    # q3
    ("q3", '=','=','R',"q5"),
    ("q3", '0','0','R',"q3"),
    ("q3", '1','1','R',"q3"),

    # q4
    ("q4", 'A','A','R',"q4"),
    ("q4", 'B','B','R',"q4"),
    ("q4", '=','=','R',"q4"),
    ("q4", '1','B','R',"q6"),
    ("q4", '0','A','L',"q0"),


    # q5
    ("q5", 'A','A','R',"q5"),
    ("q5", 'B','B','R',"q5"),
    ("q5", '=','=','R',"q5"),
    ("q5", '1','B','L',"q0"),
    ("q5", '0','A','R',"q6"),

    # q6
    ("q6", '1','B','R',"q6"),
    ("q6", '0','A','R',"q6"),
    ("q6", '=','=','L',"q7"),

    # q7
    ("q7", '0','0','L',"q7"),
    ("q7", '1','1','L',"q7"),
    ("q7", 'A','A','L',"q7"),
    ("q7", 'B','B','L',"q7"),
    ("q7", '=','=','L',"q7"),
    ("q7", '-','-','R',"q8"),

    # q8
    ("q8", '0','0','R',"q8"),
    ("q8", '1','1','R',"q8"),
    ("q8", 'A','0','R',"q8"),
    ("q8", 'B','1','R',"q8"),
    ("q8", '=','=','L',"q0")
]

modulo_transcriptor=[

    # q9
    ("q9", '=','=','R',"q9"),
    ("q9", 'A','A','R',"q9"),
    ("q9", 'B','B','R',"q9"),
    ("q9", '0','A','L',"q10"),
    ("q9", '1','B','L',"q11"),

    # q10
    ("q10", '=','=','L',"q10"),
    ("q10", 'A','A','L',"q10"),
    ("q10", 'B','B','L',"q10"),
    ("q10", '0','0','R',"q12"),
    ("q10", '1','1','R',"q12"),
    ("q10", '-','-','R',"q12"),


    # q11
    ("q11", '=','=','L',"q11"),
    ("q11", 'A','A','L',"q11"),
    ("q11", 'B','B','L',"q11"),
    ("q11", '0','0','R',"q13"),
    ("q11", '1','1','R',"q13"),
    ("q11", '-','-','R',"q13"),

    # q12
    ("q12", '=','=','L',"q14"),
    ("q12", 'A','0','R',"q9"),
    ("q12", 'B','0','R',"q9"),

    # q13
    ("q13", '=','=','L',"q15"),
    ("q13", 'A','1','R',"q9"),
    ("q13", 'B','1','R',"q9")
]

modulo_simulador = [
    # q14
    ("q14", '0','0','L',"q16"),
    ("q14", '1','1','L',"q17"),

    # q15
    ("q15", '0','0','L',"q18"),
    ("q15", '1','1','L',"q19"),

    # q16
    ("q16", '1','1','L',"q16"),
    ("q16", '0','0','L',"q16"),
    ("q16", '-','-','L',"q16"),
    ("q16", '*','0','R',"q20"),

    # q17
    ("q17", '1','1','L',"q17"),
    ("q17", '0','0','L',"q17"),
    ("q17", '-','-','L',"q17"),
    ("q17", '*','1','R',"q20"),

    # q18
    ("q18", '1','1','L',"q18"),
    ("q18", '0','0','L',"q18"),
    ("q18", '-','-','L',"q18"),
    ("q18", '*','0','L',"q20"),

    # q19
    ("q19", '1','1','L',"q19"),
    ("q19", '0','0','L',"q19"),
    ("q19", '-','-','L',"q19"),
    ("q19", '*','1','L',"q20"),


    # q20
    ("q20", '0','*','R',"q21"),
    ("q20", '','*','R',"q21"),
    ("q20", '1','*','R',"q22"),

    # q21
    ("q21", '1','1','R',"q21"),
    ("q21", '0','0','R',"q21"),
    ("q21", '-','-','R',"q21"),
    ("q21", '=','=','L',"q23"),

    # q22
    ("q22", '1','1','R',"q22"),
    ("q22", '0','0','R',"q22"),
    ("q22", '-','-','R',"q22"),
    ("q22", '=','=','L',"q24"),

    # q23
    ("q23", '0','0','R',"q25"),
    ("q23", '1','0','R',"q25"),

    # q24
    ("q24", '0','1','R',"q25"),
    ("q24", '1','1','R',"q25"),

    # q25
    ("q25", 'A','A','R',"q25"),
    ("q25", 'B','B','R',"q25"),
    ("q25", '=','=','R',"q25"),
    ("q25", '0','0','L',"q26"),
    ("q25", '1','1','L',"q26"),
    ("q25", '','','L',"q26"),

    # q26
    ("q26", 'A','0','L',"q26"),
    ("q26", 'B','1','L',"q26"),
    ("q26", '=','=','L',"q26"),
    ("q26", '0','0','R',"q0"),
    ("q26", '1','1','R',"q0")
]

# Se mete configuración inicial
m.settings=modulo_localizador+modulo_transcriptor+modulo_simulador

# preparación de la memoria
m.memory=[]
# q0 00, q1 01, q2 10, L 1, R 0, 1 1, "" 0
#X#y# --> #XY#

mem="11*10-000=0000110=0110110=0101001=1011000="

m.memory.append('')# un vacio
for c in mem: # llenamos la memoria con el string mem
    m.memory.append(c)

m.memory_pointer=mem.index('-')+3 # ponemos la MT apuntando a la posición inicial

# Bucle de ejecución animada
i=0
while m.execute():
    os.system("clear") # si se usa windows cambiar por el cls o el comando de limpieza de terminal correspondiente
    
    # esto identifica en que parte de la MTU se encuenta
    estado=int(m.current_state[1:])
    if estado > 13:
        modulo="Simulador"
        t=0.04
    elif estado > 8:
        modulo="Transcriptor"
        t=0.04
    else:
        modulo="Localizador"
        t=0.04

    # se imprime la maquina
    print "Paso - "+str(i)+" M."+modulo
    print m
    
    i+=1 # aumento de contador de pasos
    time.sleep(t) # tiempo de visualización de cada paso 0.04 s --> 25fps

