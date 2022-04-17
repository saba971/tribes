import os
from os import path

n=input(r"enter path:")
#n=r"C:\Users\thambara\Desktop\question-custom-takehome-project-ruqx1k781e-tribes_ai_data_engineer_assignment\migration_data_test"
x=os.walk(n)
lst1=[]
lst2=[]
lst3=[]
#grepping the files from the eneterd path
for i in x:
    lst1.append(i[2])
for i in range(0,len(lst1[0])):
    if ".py" in lst1[0][i]:
        lst2.append(lst1[0][i])

#filtering the files
for j in lst2:
    p=path.join(n,j)
    for line in open(p,"r+"):
        if "revision =" in line:
            lst3.append(j+":"+line)
        elif "down_revision" in line:
            lst3.append(j+":"+line)

lst3=[i.strip("\n") for i in lst3]
lst4=[]
for k in lst2:
    z=""
    for m in lst3:
        if k in m:
            l=m.split(":")[1]
            z=z+":"+l
    lst4.append(k+""+z)
lst5=[]

#function to determine the migration format
def mig(lstq):
    for i in lstq:
        v=i.split(":")[1].split("revision =")[1].strip()
        for j in lstq:
            u=j.split(":")[2].split("down_revision =")[1].strip()
            if v in u:
                g=j.split(":")[1].split("revision =")[1].strip()
                lst5.append(v+"("+i.split(":")[0]+")->"+g+"("+j.split(":")[0]+")")
                break
    return lst5

e=mig(lst4)
for i in e:
    print(i)

