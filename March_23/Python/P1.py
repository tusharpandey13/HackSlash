#When the Sepratist Next Attack

def get_score():
    code=input()
    c=2
    flag=0
    code_dict={}
    for j in range(len(code)):
        try:
            _=code_dict[code[j]]
        except:
            if flag==0:
                code_dict[code[j]]=1
                flag+=1
            elif flag==1:
                code_dict[code[j]]=0
                flag+=1
            else:
                code_dict[code[j]]=c
                c+=1
    base=max(len(code_dict),2)
    #secs=float(0)
    secs=0
    c=0
    for j in range(len(code)-1,-1,-1):
        secs+=((base**c)*code_dict[code[j]])
        c+=1
    print(secs)
    #print(int(10**18))
    
def main():
    n=int(input())
    for i in range(n):
        get_score()

main()