from calculator import calculate

def main():
    equation = input("Enter the expression\n") # Takes user input 
    answer = calculate(equation) # calculates result of expression 
    print(f"Answer:{answer}")
    
    # To use calculate function directly in code 
    
    # equation = "4+5*8/2(830-23)/13+2423-1100+2^7-23*9^0.5"  
    # answer = calculate(equation) # calculates result of expression 
    # print(f"Answer:{answer}")

if __name__ == "__main__": main()