# استقبال الرقم الاول والرقم التاني مع تحويلها من نصوص الى ارقام صحيحه وعشريه 


num1 = float(input("Enter the first number:\n"))
num2 = float(input("Enter the second number:\n"))

# العمليات الحسابية : الجمع والطرح والضرب والقسمة 
addition = num1 + num2 # الجمع 
subtraction = num1 - num2 # الطرح 
multiplication = num1 * num2 # الضرب 
division = num1 / num2 # القسمة

# طباعة العمليات بشكل جيد ومنظم
print("\n", "=" * 10, "CALCULATOR RESULT", "=" * 10)
print("First Number:\t", str(num1))
print("Second Number:\t", str(num2))
print("_" * 60)

# طباعة النتائج للعمليات
print("Addition (+):\t\t", str(addition))
print("Subtraction (-):\t\t", str(subtraction))
print("Multiplication (*):\t\t", str(multiplication))
print("Division (/):\t\t",str(division))
print("=" * 50)