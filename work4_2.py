f_n=int(input(""))
f_0=0
f_1=1
for i in range (f_n):
    print(f_0)
    f_0,f_1= f_1,f_1+ f_0
