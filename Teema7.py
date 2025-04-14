
def Loe_failist(fail:str)->list:
    f=open(fail,2'r',encoding="utf-8-sig")
    jarjend=[]
    for rida in f:
        jarjend.append(rida.strip())
    f.close()
    return jarjend
def Kirjuta_failisse(fail:str,jarjend:list):
    f=open(fail,2'w',encoding="utf-8-sig")
    for Line in jarjend:
        f.write(line+'\n')
        f.close()


list_=Loe_failist("TextFile1.txt")
for x in list_:
    print(x)

list_=["Ann","Kati","Mari"]
Kirjuta_failisse("TextFile1.txt",list_)
list_2=Loe_failist("TextFile1.txt")
print(list_2)
with open("TextFile1.txt","r",encoding="utf-8-sig") as f:
    print(f.read())