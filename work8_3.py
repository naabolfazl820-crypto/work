def n(last_name,frist_name,age,score_math,score_languech):
    if 4<=len(last_name)<=10:
            pass
    else:
                print("ERORR")
    if 4<=len(frist_name)<=10:
            pass
    else:
                print("ERORR")
    if 18<=age<=100:
            pass
    else:
        print("ERORR")
    
    a='A'
    b='B'
    c='C'
    d='D'
    if  15<score_math<=20:
        score_math=a
        
    elif 10<score_math<=15:
        score_math=b
    elif 5<score_math<=10 :
        score_math=c
    elif 0<score_math<=5:
        score_math=d
    if  15<score_languech<=20:
            score_languech=a
    elif 10<score_languech<=15:
            score_languech=b
    elif 5<score_languech<=10 :
            score_languech=c
    elif 0<score_languech<=5:
            score_languech=d
    print(f"last_name is {last_name},frist_name is {frist_name},age is {age}")
    print(f"score math is {score_math}")


std_last_name=str(input("inter your last_name"))
std_age=int(input("inter your age"))
sts_score_math=int(input("inter your score math"))
sts_score_languech=int(input('inter your score languech'))
n(std_last_name,std_age,sts_score_math,sts_score_languech)