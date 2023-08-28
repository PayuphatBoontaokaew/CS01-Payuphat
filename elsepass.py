num1 = int(input('ตัวเลขที่ 1 : '))
num2 = int(input('ตัวเลขที่ 2 : '))
num3 = int(input('ตัวเลขที่ 3 : '))

if num1 > num2 and num1 > num3 :
    print('num1 is the most : ' , num1 )

elif num2 > num1 and num2 > num3 :
    print('num2 is the most')
elif num3 > num1 and num3 > num2 :
    print("num3 is the most")
else :
    print('เจ๊ง') 
    