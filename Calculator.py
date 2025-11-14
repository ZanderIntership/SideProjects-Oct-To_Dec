
import operator

IntialValue = 0
SecondValue = 0
CompoundingValue = 0

EndLoop = False

operators = ["+", "-", "*", "/", "%", "//", "**"]

op_map = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "%": operator.mod,
    "//": operator.floordiv,
    "**": operator.pow,
}

Symbole = ""

prompt = "";

IntialValue = float(input("Please Enter your first value : "))
SecondValue = float(input("Please Enter your second value : "))
ReturnValue = 0
Symbole = input("Please Enter your symbol : ")

for I in range(0,len(operators)):
    if operators[I] == Symbole:
        ReturnValue = op_map[operators[I]](IntialValue,SecondValue)
        print(ReturnValue)

prompt = input("Would you like to continue? (Y/N) : ")
if prompt == "N" or prompt == "n":
    EndLoop = True;
    exit()
else:
    pass

while not EndLoop:
    CompoundingValue = float(input("Please Enter your compounding value : "))
    Symbole = input("Please Enter your symbol : ")

    for I in range(0, len(operators)):
        if operators[I] == Symbole:
            ReturnValue = op_map[operators[I]](ReturnValue, CompoundingValue)
            print(ReturnValue)

    prompt = input("Would you like to continue? (Y/N) : ")

    if prompt == "N" or prompt == "n":
        EndLoop = True;
        exit()
    else:
        pass
