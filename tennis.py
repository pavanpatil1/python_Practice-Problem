server = 0
op = 0
ch =0
print("---------------------------------")
print("1.Decide the Winner \n2.Exit")
print("---------------------------------")
ch = input("Enter your Choice")
if ch == 1:
        while True:
            p = raw_input("Who win Set")
            if (p == "s" and server<30):
                server += 15
              

            elif(p == "s" and server <= 40 and server == 30):
                server += 10


            elif( p == "s" and server >= 40):
                server +=1
                r = server - op
                if(r>=2):
                    print server,op
                    print "server win the Match"
                    exit()

                

            elif(p == "o" and op < 30):
                op +=15
               

            elif p == "o" and op == 30 and op <40:
                op +=10
               


            elif p == "o" and op >= 40:
                op +=1
                r1 = op - server
                if(r1 >= 2):
                    print "Opponenent Win the Match"

            if(p > 40 and op > 40 and server == op):
                server = 40
                op = 40
                print (server , op)
            else:
                print server,op

            
            


            



    



