marksheet=[]
scorelist=[]
if __name__ == '__main__':
        for _ in range(int(input())):
                name = input()
                score = float(input())
                marksheet+=[[name,score]]
                scorelist+=[score]
        p = sorted(list(scorelist))[1]
        for i,b in sorted(marksheet):
            if b == p:
                print(i) 
        
