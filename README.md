# Calculate Expression

## A mathematical expression evalutor in Python 

This Python script can evaluate mathematical expressions. The user can input 
a string containing the expression into the calculate function and the program 
will evaluate the expression and return the answer as a string. It uses a basic
parsing algorithm to parse the inputted string and process it into a list of 
terms that is then evaluated in accordance to PEMDAS. 

## How to use it 

1) Clone this project. This will give you the main.py and calculator.py files 
2) Run the main.py file to get a input prompt in the terminal. There you
can type in an expression and it will be evaluated the printed in the terminal
3) Alternatively, the calculator.py file can be used in other projects and 
folders

``` python
from calculator import calculate 
expression = "3+4*8"
print(calculate(expression))
```

