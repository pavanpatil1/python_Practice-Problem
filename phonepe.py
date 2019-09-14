b = 0
while True:
    print("\n----------------Welcome to PhonePe----------------------")
    print("1. Create Account \n2.Login \n3.Exit ")
    print("---------------------------------------------------------")

    ch = input("Enter your Choice")
    if ch == 1:
            print("\n\n----------------Welcome to PhonePe----------------------")
            u = raw_input("Enter your Username")
            e = raw_input("Enter your Email")
            p = raw_input("Enter your Password")
            print("\n -- Thanks For Register in PhonePe -- ")
    
    if ch == 2:
            i = raw_input("Enter Username ")
            o = raw_input("Enter Password ")
            if (i == u and o == p):
                while True:
                    print("\n--------------------------------------")
                    print "Welcome User",i 
                    print(" Your PhonePe Account \n1.Transfer Money \n2. Add Money \n3.Check Balance \n4.Logout")
                    print("---------------------------------------")
                    ch1  = input("Enter your Choice")
                    list1 = []
                    if ch1 == 1:
                        a = input("Enter the Mobile Number")
                        r = input("Enter Amount")
                        b = b - r
                        print "Your Remaining Balance is",b

                    if ch1 == 2:
                        k = input("Enter Amount to Add")
                        b +=k
                        print "Your Balance is Ruppes",b

                    if ch1 == 3:
                        print "Your Balance is Ruppes",b

            
                    if ch1 == 3:
                        break
