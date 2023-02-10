#!python3
# Calculate an integral based on upper and lower bounds
# Function is defined in Fofx
# Left, Right, Midpoint and Trapezoidal Reimann sums are calculated
import math

def Fofx(x):
    # Define your function here
    y = math.e**x
    return y


def getInput(question,type):
    valid = False
    myType = {
        "integer" : int,
        "float" : float,
        "string": str
    }        
    while valid == False:
        inp = input(f"{question} (should be a {type}):")
        try:
            val = myType[type](inp)
            return val
        except:
            print('invalid response')

def calcIntegral(a,b,n):
    dx = (b-a)/n
    LSum = 0
    RSum = 0
    MSum = 0
    TSum = 0
    for i in range(n):
        h = Fofx(a+i*dx)
        LSum += dx*h
    
        h = Fofx(a+(i+1)*dx)
        RSum += dx*h
    
        h = Fofx( (a+i*dx + a+(i+1)*dx)/2 )
        MSum += dx*h

        h = (Fofx(a+i*dx) + Fofx(a+(i+1)*dx))/2
        TSum += dx*h
    
    return {"L" : LSum, "R": RSum, "M": MSum, "T":TSum}

def main():
    print("Left Reimann Approximation")
    a = getInput("Enter the lower bound","float")
    b = getInput("Enter an upper bound","float")
    n = getInput("How many intervals between a and b","integer")
    Area = calcIntegral(a,b,n)
    print(f"The area under the curve between {a} and {b} is {Area}")
        


if __name__ == "__main__":
  main()
