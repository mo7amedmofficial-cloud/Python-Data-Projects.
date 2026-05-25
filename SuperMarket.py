# فاتورة لبيع منتج جديد 
ProductName = input("Enter the product name:\n") # اسم المنتج 
product_price = input("Enter the product price:\n") 
quantityrequired = input("Enter the required quantity of the product:\n")
total = int(product_price)*int(quantityrequired) # اتحويل النص الى رقم عشان تحصل عملية الضرب 
print("=== CASH RECEIPT ===")
print("Product Name:\t" + "["+ ProductName +"]")
print("Quantity:\t" + quantityrequired)
print("Total Price:\t" + str(total) + "$")
