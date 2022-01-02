import functions_list
'''
Instead of importing file, you can also do this


You could use this script:

def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read())

Syntax:

run("file.py")
###############################
There are multiple ways to make one Python file run another.

1. Use it like a module. import the file you want to run and run its functions. For example, say you want to import fileB.py into fileA.py, assuming the files are in the same directory, inside fileA you'd write

import fileB

Now in fileA, you can call any function inside fileB like:

fileB.my_func()

2. You can use the exec command. 

execfile('file.py')

 executes the file.py file in the interpreter.

3. You can spawn a new process using the os.system command.
For example

os.system('python my_file.py')
'''


#Check if you can use the functions from the functions_list file
a = functions_list.isprime(9)
print(a)