from DecodeFunction import decode
from ExitFunction import exit_program
from function_parser import parse_function

import msvcrt

functions = (("Decode file", decode), ("Exit program", exit_program))

print("\nWelcome to a virtual machine! Please select one of the functions")
for index, item in enumerate(functions, start=1):
    print(str(index) + ". " + str(item[0]))

# Replace with msvcrt.getch()
selection = msvcrt.getch()
parse_function(functions, selection)





