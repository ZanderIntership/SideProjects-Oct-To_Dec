#Beginner Level
#Level 1, Sum of dgits
    num1,num2 = 1,2
    print(f'{num1 + num2}')

#Level 2 Fibonacci Sequence

lengthh = input('How lomg do you want the Fibonacci series?')
start = 1
FibonaciSeq = [1]

for I in range(int(lengthh)):
    start = FibonaciSeq[I] + FibonaciSeq[I - 1]
    FibonaciSeq.append(start)
    print(FibonaciSeq[I])

#Level 3 ArmStrong calcilator

IntialValue = input("Enter initial value")
ValueHolder = []
FinaleValueHolder = 0

for i in range(len(IntialValue)):
    ValueHolder.append(int(IntialValue[i]))
    FinaleValueHolder += pow(ValueHolder[i],len(str(IntialValue)))
    print(FinaleValueHolder)

if FinaleValueHolder == int(IntialValue):
    print("This is a ArmStrongValue")
else:
    print("This is not a ArmStrongValue")
