# حماية وتنسيق البريد الالكتروني 
# اطلب من المستخدم ادخال اسمه كاملا وبريده الالكتروني 
CuName = input("Enter Your Full Name:\n") # مثال : Mhamed Ahmed
e_mail = input("Enter Your Email:\n") # مثال: mohamed2026@gmail.com
part1 = CuName[0:3]
part2 = e_mail[0:3]
user_name = part1 +'_'+ part2
# طباعة البيانات بشك منظم
# اولا رأس البيان
print("=" * 50)
print("\t ACCOUNT CUSTOMER RECEIPT")
print("=" * 50)
print("")
print(" * Customer Name:\t" + CuName.upper())
print(" * Secured Email:\t" + e_mail[:3] + "*****" + "@gmail.com")
print(" * Generated Username:\t" + user_name)
print('')
print("-" * 50)
print("Thank you for registering\n")
input("Press Enter To Exit")
