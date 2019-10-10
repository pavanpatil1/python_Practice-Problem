def fun():

    p = open('p.txt','r')
    print(p.read())

    while True:
        n = input("Enter your Choice = ")
        if n in p:
            print("You Choosen string as" , n)
            break
        else:
            print("Ohh !! Wrong Entry")

        

    s = input("Enter a Substring from the Choosen string = ")
    print("You Choosen the Substring as a ",s)
    dfa = input("Enter a string for an Check an DFA = ")
    if s not in dfa:
        print("String is not Accepted")
    else:
        print("Accepted")

z = fun()
print(z)