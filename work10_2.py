

from modul_work10_1 import jam


# main.py - برنامه محاسبه BMI با استفاده از ماژول ماشین حساب

# 📌 مرحله ۱: وارد کردن ماژول
import modul_work10_1
print("=" * 45)
print("🏥 برنامه محاسبه شاخص توده بدنی (BMI)")
print("=" * 45)
print("فرمول: BMI = وزن (کیلوگرم) ÷ (قد (متر))²")
print("-" * 45)

# 📌 مرحله ۲: دریافت اطلاعات از کاربر
while True:
    try:
        vazn = float(input("📥 وزن خود را به کیلوگرم وارد کنید: "))
        ghad_cm = float(input("📥 قد خود را به سانتی‌متر وارد کنید: "))
        
        if vazn <= 0 or ghad_cm <= 0:
            print("❌ وزن و قد باید عدد مثبت باشند!\n")
            continue
        break
    except ValueError:
        print("❌ لطفاً فقط عدد وارد کنید.\n")

# 📌 مرحله ۳: تبدیل قد از سانتی‌متر به متر
# با استفاده از تابع taghsim از ماژول calculator
ghad_metr = modul_work10_1.taghsim(ghad_cm, 100)
print(f"\n📏 قد شما به متر: {ghad_metr}")

# 📌 مرحله ۴: محاسبه توان دوم قد (قد × قد)
# با استفاده از تابع zarb از ماژول calculator
ghad_be_tavan_2 = modul_work10_1.zarb(ghad_metr, ghad_metr)
print(f"📐 (قد)² = {ghad_be_tavan_2}")

# 📌 مرحله ۵: محاسبه BMI
# با استفاده از تابع taghsim از ماژول calculator
bmi = modul_work10_1.taghsim(vazn, ghad_be_tavan_2)

print("\n" + "=" * 45)
print(f"🎯 شاخص توده بدنی (BMI) شما: {bmi:.2f}")
print("=" * 45)

# 📌 مرحله ۶: تفسیر نتیجه با استفاده از تابع tafrigh برای محاسبه فاصله تا حد نرمال
print("\n📋 تفسیر نتیجه:")

if bmi < 18.5:
    print("⚠️  وضعیت: کمبود وزن")
    # محاسبه فاصله تا حد نرمال با تابع tafrigh
    fasele = modul_work10_1.tafrigh(18.5, bmi)
    print(f"   📊 فاصله شما تا حد نرمال: {fasele:.2f}")
    
elif bmi < 25:
    print("✅ وضعیت: وزن نرمال - آفرین! 🎉")
    print("   📊 شما در محدوده سالم قرار دارید.")
    
elif bmi < 30:
    print("⚠️  وضعیت: اضافه وزن")
    fasele = modul_work10_1.tafrigh(bmi, 25)
    print(f"   📊 فاصله شما از حد نرمال: {fasele:.2f}")
    
else:
    print("🚨 وضعیت: چاقی")
    fasele = modul_work10_1.tafrigh(bmi, 25)
    print(f"   📊 فاصله شما از حد نرمال: {fasele:.2f}")

# 📌 مرحله ۷: محاسبه وزن ایده‌آل (حد وسط محدوده نرمال = 21.7)
vazn_ideal = modul_work10_1.zarb(21.7, ghad_be_tavan_2)
print(f"\n💡 وزن ایده‌آل تقریبی شما: {vazn_ideal:.2f} کیلوگرم")

# 📌 مرحله ۸: محاسبه تفاوت وزن فعلی با وزن ایده‌آل
taghirat = modul_work10_1.tafrigh(vazn, vazn_ideal)
print(f"📊 تفاوت وزن فعلی شما با وزن ایده‌آل: {taghirat:.2f} کیلوگرم")

print("\n👋 ممنون که از برنامه استفاده کردید!")