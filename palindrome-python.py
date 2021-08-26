import pandas as pd
import string
import re
import numpy as np

data=pd.read_excel(r"C:\Users\nigbu\Desktop\isimler.xlsx")
mylist = data['isimler'].tolist()
pali_list=[]
data.isimler
length=len(mylist)
for x in range(0,length):
    print("Reverse of the "+mylist[x]+": "+mylist[x][::-1])
    if(mylist[x][::-1]==mylist[x]):
        print("\nPalindrome is found: "+mylist[x][::-1]+"\n")
        pali_list.append(mylist[x])
        
pali_length=len(pali_list)
text_str=""
for i in range(0,pali_length):
    text_str=pali_list[i]
    n_list=list(text_str.encode())
    num_list=np.add(n_list,-96).tolist()
    print(f"{num_list=} --> "+pali_list[i]+" --> Numeric value: "+str(sum(num_list)))
    