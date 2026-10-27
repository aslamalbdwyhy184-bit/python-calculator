print("اختر العملية الحسابية:")
print("1. جمع (+)")
print("2. طرح (-)")
print("3. ضرب (*)")
print("4. قسمة (/)")

choice = input("أدخل رقم العملية (1/2/3/4) : ")

num1 = float(input("أدخل الرقم الأول: "))
num2 = float(input("أدخل الرقم الثاني: "))

if choice == '1':
    result = num1 + num2
    print(f"النتيجة: {num1} + {num2} = {result}")
elif choice == '2':
    result = num1 - num2
    print(f"النتيجة: {num1} - {num2} = {result}")
elif choice == '3':
    result = num1 * num2
    print(f"النتيجة: {num1} * {num2} = {result}")
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"النتيجة: {num1} / {num2} = {result}")
    else:
        print("خطأ: لا يمكن القسمة على الصفر!")
else:
    print("إدخال غير صحيح")
  
