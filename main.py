canswer = 'Yes'
while canswer != 'No':
    print("What is your first number?")
    first = float(input())

    print("What is your second number?")
    second = float(input())




    print("What do you want to do?")
    print("a = add")
    print("s = substraction")
    print("m = multiplication")
    print("d = division")
    answer = input()

    if answer == 'a' :
        addnumber = first + second
        print(addnumber)

    if answer == 's':
        subnumber = first - second
        print(subnumber)

    if answer == 'm':
        mulnumber = first * second
        print(mulnumber)

    if answer == 'd':
        divnumber = first / second
        print(divnumber)



    
    print('Would you like to continue(Yes/No)?')
    canswer = input()

    #e