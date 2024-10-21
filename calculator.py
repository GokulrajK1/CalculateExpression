import math

# Constants 
operators = "+-*/^?"
digits = "0123456789."
startBrackets = "({["
endBrackets = ")}]"
numFound = False

# Parses through equation and converts expression string into a list of numbers and operators 
# Also adds additional numbers or operators to process the list properly for calculation 
def parseEquation (eq : str):
    nEQ = "+" + eq + "?"
    term = ""
    terms = []
    num = 0.0
    swap = 1.0
    index = 0
    global numFound
    
    for char in nEQ:
        if char in operators or char in endBrackets:
            if char == "?" and terms[-1] == ")":
                terms.append(char)
                break
            if term != "":
                num = float(term) * swap
                swap = 1.0
                term = ""
                if terms[-1] in endBrackets:
                    terms.append("*")
                terms.append(str(num))
            terms.append(char)
        
        elif char in digits:
            numFound = True
            term += char
        
        elif char == "~":
            swap *= -1.0
        
        elif char in startBrackets:
            if index == 0:
                terms.append("0.0")
                terms.append("+")
            elif term != "":
                num = float(term) * swap
                swap = 1.0
                term = ""
                if terms != []:
                    if terms[-1] in endBrackets and terms != []:
                        terms.append("*")
                terms.append(str(num))
                terms.append("*")
            elif terms[-1] in endBrackets:
                terms.append("*")
                terms.append("1.0")
                terms.append("*")
            elif swap == -1.0:
                if terms[-1] in "+-*":
                    terms.append("-1.0")
                    terms.append("*")
                    swap = 1.0
                elif terms[-1] == "^":
                    terms.append("-1.0")
                    terms.append("^")
                    swap = 1.0
                elif terms[-1] == "/":
                    terms.append("-1.0")
                    terms.append("/")
                    swap = 1.0
            terms.append(char)
        elif char == " ":
            pass
        else:
            print(char)
            raise SyntaxError
        index += 1
    terms.pop()
    return terms


# Checks for special cases where there is no number inputed or two operators in a row or a
# mismatch of opening and closing paranetheses 
def opError (terms: list):
    if not numFound:
        raise SyntaxError
    index = 0
    term = ""
    nextTerm = ""
    if len(terms) <= 1:
        return terms
    while (index + 1 < len(terms)):
        term = terms[index]
        nextTerm = terms[index + 1]
        if term in operators and nextTerm in operators:
            raise SyntaxError
        index += 1
    
    left = 0
    right = 0
    for t in terms:
        if t in startBrackets:
            left += 1
        elif t in endBrackets:
            right += 1
    if left != right:
        raise SyntaxError
    return terms

# Uses the processed list and evaluates the terms in the list in accordance with PEMDAS
def solveEquation (terms: list):
    global operators
    if operators[-1] == "?":
        operators = "+-*/^"
    if terms.count == 0:
        raise SyntaxError
    pTerms = []
    eTerms = []
    mdTerms = []
    term = ""
    computedTerm = 0.0
    answer = 0.0
    
    #Parenthesis Solve: Uses recursion to evaluate the expressions in parentheses by calling solveEquation
    while len(terms) > 0:
        term = terms.pop(0)
        if term in startBrackets:
            computedTerm = solveEquation(terms)
            terms.insert(0, str(computedTerm))
        elif term in endBrackets:
            break
        else:
            pTerms.append(term)
    
    pre = 0.0
    next = 0.0
    holder = 0.0
    
    #Exponent Solve: Whenever encountering ^, finds the terms before and after and calculates using pow function
    while (len(pTerms) > 0):
        term = pTerms.pop(0)
        if term == "^":
            if p := float(eTerms.pop()):
                if n := float(pTerms[0]):
                    pTerms.pop(0)
                    holder : int = pow(p, n)
                    if math.isnan(holder):
                        if (1/n) % 2 == 1:
                            holder = -pow(p * -1, n)
                            pTerms.insert(0, str(holder))
                    
                        else:
                            raise ArithmeticError
                
                    else:
                        pTerms.insert(0, str(holder))
        else:
            eTerms.append(term)
    
    #print(eTerms, "E") Uncomment if you want to debug
    
    #Multiplication and Divison Solve: whenever encountering * or /, pops the term before and after and calculates 
    while len(eTerms) > 0:
        term = eTerms.pop(0)
        if term in "*/":
            if p := float(mdTerms.pop()):
                if n := float(eTerms[0]):
                    if term == "/":
                        if n == 0:
                            raise ZeroDivisionError
                        else:
                            n = 1/n
                    eTerms.pop(0)
                    eTerms.insert(0, str(p * n))
        else:
            mdTerms.append(term)
    
    #print(mdTerms, "MD") Uncomment if you want to debug
    
    if mdTerms[0] != "+":
        mdTerms.insert(0, "+")
    
    # Addition and Subtraction Solve: converts subtraction to adding negative term and then sums all 
    # remaining terms together to calculate the final answer 
    swap = 1.0
    
    while len(mdTerms) > 0:
        term = mdTerms.pop(0)
        if term == "-":
            swap = -1.0
        if term in "+-":
            if p := float(mdTerms[0]):
                answer += p * swap
                swap = 1.0
    
    
    #print(answer, "AS") Uncomment if you want to debug
    
    return answer

# Calculate Function: returns the answer given a mathematical expression in form of a string 
def calculate (equation : str):
    global operators, numFound
    parsed = parseEquation(equation)
    opChecked = opError(parsed)
    answer = solveEquation(opChecked)
    operators = "+-*/^?"
    numFound = False
    return str(answer)


