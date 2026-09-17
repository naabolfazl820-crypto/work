def student_management_system():
    # دیکشنری کاربران (کلید: یوزرنیم، مقدار: پسورد)
    users = {"abolfazl": "abolfazl112", "alireza": "aliraza112"}
    
    # د
    students = {
        "abolfazl": {"password": "abolfazl112", "score": 20, "last_name": "Ahmadi"}
    }

    # مرحله لاگین
    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username] == password:
        print(f"\nخوش آمدید {username} عزیز!")
        
        while True:  # استفاده از حلقه  برای منو
            print("\n--- MENU---")
            print("1. infomation student")
            print("2. add new student")
            print("3. exite")
            
            choice = input("choise ")

            if choice == '1':
                print(students)
            elif choice == '2':
                new_user = input("new user ")
                new_pass = input("new password ")
                new_last_name = input("last_name ;  ")
                new_score = input("score :  ")
                
                students[new_user] = {
                    "password": new_pass, 
                    "last_name": new_last_name, 
                    "score": new_score
                }
                print("moafagh")
            elif choice == '3':
                print("exite in system")
                break
            else:
                print("erorr namotabar")
    else:
        print("user or password eshtebah")

student_management_system()