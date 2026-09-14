def std(first_name, last_name, age, ctr, score_1, score_2):
  
    if not (3 <= len(first_name) <= 10):
        return "ERROR: Your first name length should be between 3 and 10."
    
    
    if not (3 <= len(last_name) <= 10):
        return "ERROR: Your last name length should be between 3 and 10."
    
  
    if not (18 <= age <= 1000):
        return "ERROR: The system is unable to respond to you (Invalid age)."

   
    def get_grade(score, subject_name):
        if 15 < score <= 20:
            return f"Your {subject_name} score is A: {score}"
        elif 10 < score <= 15:
            return f"Your {subject_name} score is B: {score}"
        elif 5 < score <= 10:
            return f"Your {subject_name} score is C: {score}"
        elif 0 <= score <= 5:
            return f"Your {subject_name} score is D: {score}"
        else:
            return f"ERROR: Cannot read your {subject_name} score."

    grade_1 = get_grade(score_1, "Math")
    grade_2 = get_grade(score_2, "English")
    

    return f"""
--- Student Report ---
Name: {first_name} {last_name}
Age: {age}
Country: {ctr}
{grade_1}
{grade_2}
----------------------
"""


print("Please enter student information:")
std_first_name = input("Enter your first name: ")
std_last_name = input("Enter your last name: ")

try:
    std_age = int(input("Enter your age: "))
    std_ctr = input("Enter your country: ")
    std_score_1 = float(input("Enter your Math score: "))
    std_score_2 = float(input("Enter your English score: "))
    
    
    print(std(std_first_name, std_last_name, std_age, std_ctr, std_score_1, std_score_2))

except ValueError:
    print("ERROR: Please enter valid numbers for age and scores.")

file=open("std_information","a")
file.write(f"\n frist name is : {std_first_name} and last name is : {std_last_name} and age is : {std_age} and ctr is : {std_ctr} and score math is : {std_score_1} and score languech is : {std_score_2}")
file.close
file=open("std_information","r")
print(file.read())
file.close
