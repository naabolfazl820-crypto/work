
name=str(input("name vared kon :"))
last_name=str(input("last name vared kon :"))
age=int(input("age vared kon :"))
ctr=str(input("ctr vared kon :"))
score=int(input("score vared kon :"))
a=3
s=100
d=5
aa='A'
dd="D"
bb="B"
cc='C'
ff='F'
ee='E'
for i in range(s):
    if 3<=len(name)<=10:
       # print(name)
        break

for b in range (s):
    if 3<=len(last_name)<=10:
        #print(last_name)
        break
for w in range(s):
    if 10<age<=50:
       # print(age)
        break

for h in range(s):
    if 18<score<=20:
      score=aa
    
      break
    elif 16<score<=18:
        score=bb
        break
    elif 14<score<=16:
        score=cc
        break
    elif 12<score<=14:
        score=dd
        break
    elif 10<score<=12 :
        score=ee
        break
    elif 1<score<=10:
        score=ff
        break


std={"name":name,"lastname":last_name,"age":age,"ctr":ctr,"score":aa,"score":dd,"score":bb,"score":cc,"score":ee,"score":ff}
print(std["name"])
print(std["score"])