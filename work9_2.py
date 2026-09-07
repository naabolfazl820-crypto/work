def calculate_circle_area(radius):
    # تعریف عدد پی به صورت دستی
    PI = 3.14159
    
    if radius < 0:
        return "خطا: شعاع نمی‌تواند منفی باشد!"
    
    # محاسبه مساحت: پی * شعاع به توان ۲
    area = PI * (radius ** 2)
    return area

# دریافت ورودی از کاربر
user_input = input("شعاع دایره را وارد کنید: ")

try:
    r = float(user_input)
    result = calculate_circle_area(r)
    
    # بررسی اینکه آیا نتیجه یک عدد است یا پیغام خطا
    if isinstance(result, str):
        print(result)
    else:
        print(f"مساحت دایره با شعاع {r} برابر است با: {result:.2f}")

except ValueError:
    print("خطا: لطفاً فقط عدد وارد کنید.")