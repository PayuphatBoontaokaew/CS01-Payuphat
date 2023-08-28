# num = int(input("in put num :"))
# for i in range(1,13):
#     result = num * i
#     print(f"{num} = {result}")

total = 0
for i in range(10):
    num = int(input("ใส่ตัวเลขครับ :"))
    if num < 0 :
        print('ไม่นับเลขลบครับ!! ')
        continue

    total+= num 


print('รวมเลขครับ' , total)

    


