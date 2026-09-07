
def universal_calculator():
    print("--- ماشین‌حساب جامع (همه در یک تابع) ---")
    
    # ۱. دریافت عملگر
    op = input("یک عملگر انتخاب کنید (+, -, *, /): ")
    if op not in ['+', '-', '*', '/']:
        print("عملگر نامعتبر است!")
        return

    # ۲. دریافت اعداد از کاربر
    numbers = []
    print("اعداد را وارد کنید (برای پایان 'تمام' را بنویسید):")
    while True:
        val = input(f"عدد {len(numbers) + 1}: ")
        if val.lower() == 'تمام':
            break
        try:
            numbers.append(float(val))
        except ValueError:
            print("لطفاً فقط عدد وارد کنید.")

    # بررسی اینکه حداقل یک عدد وارد شده باشد
    if not numbers:
        print("هیچ عددی وارد نشد.")
        return

    # ۳. انجام محاسبات داخل همین تابع
    result = 0
    if op == '+':
        result = sum(numbers)
    elif op == '-':
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
    elif op == '*':
        result = 1
        for num in numbers:
            result *= num
    elif op == '/':
        result = numbers[0]
        for num in numbers[1:]:
            if num == 0:
                print("خطا: تقسیم بر صفر امکان‌پذیر نیست!")
                return
            result /= num
            
    print(f"--- نتیجه نهایی: {result} ---")

# اجرای برنامه
universal_calculator()
