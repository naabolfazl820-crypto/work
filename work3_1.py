frist_name = str(input("name vared kon : "))
last_name = str(input("last name vared kon : "))
age = float(input("sen vared kon : "))
score = float(input(" nomre vared kon : "))
if score > 18 :
    print (" SCORE A")
    print(frist_name)
    print(last_name)
    print(age)
elif 13 < score < 18 :
    print("SCORE B")
    print(frist_name)
    print(last_name)
    print(age)
elif score < 10 :
    print("SCORE D")
    print(frist_name)
    print(last_name)
    print(age)
else :
    print(" SCORE C ")



