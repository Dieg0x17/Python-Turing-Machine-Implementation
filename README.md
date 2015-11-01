Basic Implementation of a Turing Machine in python.

Basic usage:

```
$ python
Python 2.7.9 [GCC 4.9.2] on linux2
>>> from tm import *
>>> machine=TuringMachine()
>>> machine.settings=[("q0",'1','0','R', "q0")]
>>> machine.memory=['1','1','1','']
>>> while machine.execute():
...     print machine
... 
Memory:
['0', '1', '1', '']

Memory Pointer:
M[1]-->'1'

Current State:
q0
Memory:
['0', '0', '1', '']

Memory Pointer:
M[2]-->'1'

Current State:
q0
Memory:
['0', '0', '0', '']

Memory Pointer:
M[3]-->''

Current State:
q0

```

Complex usage:

```
$ python
Python 2.7.9 [GCC 4.9.2] on linux2
>>> from tm import *
>>> machine=TuringMachine()
>>> machine.settings=[("q0",'1','0','R', "q0")]
>>> machine.memory=['1','1','1','']
>>> eh=ExecutionHandler(machine)
>>> eh.execute()

--------Step: 0--------
Memory:
['1', '1', '1', '']

Memory Pointer:
M[0]-->'1'

Current State:
q0

--------Step: 1--------
Memory:
['0', '1', '1', '']

Memory Pointer:
M[1]-->'1'

Current State:
q0

--------Step: 2--------
Memory:
['0', '0', '1', '']

Memory Pointer:
M[2]-->'1'

Current State:
q0

--------Step: 3--------
Memory:
['0', '0', '0', '']

Memory Pointer:
M[3]-->''

Current State:
q0


```

read the example.py to learn more about the configuration and execution of the universal turing machine.
