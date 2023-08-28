for i  in range(40):
    if i == 35:
        continue
    print(i)


while True :
    user_input = int(input('Enter integer :'))
    if user_input != -1:
        print('put more!!!')
    else :
        break
print('stop')