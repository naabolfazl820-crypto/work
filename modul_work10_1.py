# ۱. تعریف توابع برای عملیات ریاضی
def jam(x, y):
    return x + y

def tafrigh(x, y):
    return x - y

def zarb(x, y):
    return x * y

def taghsim(x, y):
    if y == 0:
        return "خطا: تقسیم بر صفر ممکن نیست!"
    return x / y

# ۲. نمایش منو به کاربر
print("🔢 ماشین حساب ساده پایتون 🔢")
print("عملیات مورد نظر خود را انتخاب کنید:")
print("1. جمع (+)")
print("2. تفریق (-)")
print("3. ضرب (*)")
print("4. تقسیم (/)")

# ۳. حلقه بی‌نهایت برای اینکه برنامه مدام در حال اجرا بماند
while True:
    # گرفتن انتخاب کاربر
    choice = input("\nلطفاً عدد عملیات (1/2/3/4) را وارد کنید (یا 'q' برای خروج): ")

    # شرط خروج از برنامه
    if choice.lower() == 'q':
        print("از برنامه خارج شدید. خدانگهدار! 👋")
        break

    # بررسی اینکه آیا کاربر یکی از اعداد 1 تا 4 را وارد کرده است
    if choice in ('1', '2', '3', '4'):
        
        # دریافت دو عدد از کاربر (با استفاده از try برای جلوگیری از خطا)
        try:
            num1 = float(input("عدد اول را وارد کنید: "))
            num2 = float(input("عدد دوم را وارد کنید: "))
        except ValueError:
            print("❌ ورودی نامعتبر! لطفاً فقط عدد وارد کنید.")
            continue # برگشت به ابتدای حلقه

        # انجام عملیات بر اساس انتخاب کاربر
        if choice == '1':
            print(f"✅ نتیجه: {num1} + {num2} = {jam(num1, num2)}")

        elif choice == '2':
            print(f"✅ نتیجه: {num1} - {num2} = {tafrigh(num1, num2)}")

        elif choice == '3':
            print(f"✅ نتیجه: {num1} * {num2} = {zarb(num1, num2)}")

        elif choice == '4':
            result = taghsim(num1, num2)
            print(f"✅ نتیجه: {num1} / {num2} = {result}")
            
    else:
        print("❌ ورودی نامعتبر است. لطفاً فقط 1، 2، 3 یا 4 را وارد کنید.")