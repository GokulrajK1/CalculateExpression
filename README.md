# Calculate Expression

## A mathematical expression evalutor in Python 

This Python script can evaluate mathematical expressions. The user can input 
a string containing the expression into the calculate function and the program 
will evaluate the expression and return the answer as a string. It uses a basic
parsing algorithm to parse the inputted string and process it into a list of 
terms that is then evaluated in accordance to PEMDAS. 

## Features
- Can peform addition (+), subtraction (-), multiplication (*), division (/), and exponents (^)
- Follows PEDMAS
- Can use multiple layer of parantheses 
- Can multiply using paranetheses by just doing 2(3)


## How to use it 
1) Clone this project. This will give you the __main.py__ and __calculator.py__ files 
2) Run the __main.py__ file to get a input prompt in the terminal. There you
can type in an expression and it will be evaluated the printed in the terminal
3) Alternatively, the __calculator.py__ file can be used in other projects and 
folders

## Importing the calculate function 
``` python
from calculator import calculate 
expression = "3+4*8(9-32^0.5-2)-3(3(3))"
print(calculate(expression))
# Answer is 18.98066401624382 
```

## Using negative numbers and expressions
Whenever inputting a negative number use the "~" rather than a minus sign 
DO: 2+~3 => 2 - 3 = -1
DO NOT: 2+-3 => ERROR