# for i in range(2): 
#     for j in range(2): 
#         print(i, j) 

# x = 5 
# y = x + 3 
# y *= y 
# print(y) 

# 5 == "5"

# x = 1
# while x < 4: 
#     x += 1 
#     print(x)

# score0 = str(input('กรุณาใส่คะแนนครั้งที่ 1 :'))
# if score0 == 'W':
#     print('ติด ร ')
#     break

# score1 = int(input('กรุณาใส่คะแนนครั้งที่ 1 :'))
# if score1 <= 30  :
#     print('ok')
# else :
#     print('Error โปรดใส่คะแนนอีกครั้ง')
# score2 = int(input('กรุณาใส่คะแนนครั้งที่ 2 :'))
# if score2 <= 20  :
#     print('ok')
# else :
#     print('Error โปรดใส่คะแนนอีกครั้ง') 
# score3 = int(input('กรุณาใส่คะแนนครั้งที่ 3 :'))
# if score3 <= 30  :
#     print('ok')
# else :
#     print('Error โปรดใส่คะแนนอีกครั้ง')

# score4 = int(input('กรุณาใส่คะแนนครั้งที่ 4 :'))
# if score3 <= 20  :
#     print('ok')
# else :
#     print('Error โปรดใส่คะแนนอีกครั้ง')

# score = score1 + score2 + score3 + score4
# if score >= 80 :
#     print('grade = 4')
# elif score == 'W' :
#     print('ติด ร')
# elif score >=  75 :
#     print('grade = 3.5')
# elif score >=  70 :
#     print('grade = 3')
# elif score >=  65 :
#     print('grade = 2.5')
# elif score >=  60 :
#     print('grade = 2')
# elif score >=  55 :
#     print('grade = 1.5')
# elif score >=  50 :
#     print( 'grade = 1' )
# else :
#     print('grade = 0')

# score0 = str(input('กรุณาใส่คะแนนครั้งที่ 1 :'))
# if score0 == 'W':
#     print('ติด ร ')

# score1 = int(input('กรุณาใส่คะแนนครั้งที่ 1 :'))
# if score1 <= 30:
#     print('ok')
# else:
#     print('Error โปรดใส่คะแนนอีกครั้ง')

# score2 = int(input('กรุณาใส่คะแนนครั้งที่ 2 :'))
# if score2 <= 20:
#     print('ok')
# else:
#     print('Error โปรดใส่คะแนนอีกครั้ง')

# score3 = int(input('กรุณาใส่คะแนนครั้งที่ 3 :'))
# if score3 <= 30:
#     print('ok')
# else:
#     print('Error โปรดใส่คะแนนอีกครั้ง')

# score4 = int(input('กรุณาใส่คะแนนครั้งที่ 4 :'))
# if score4 <= 20:
#     print('ok')
# else:
#     print('Error โปรดใส่คะแนนอีกครั้ง')

# score = score1 + score2 + score3 + score4
# if score >= 80:
#     print('grade = 4')
# elif score == 0:
#     print('ติด ร')
# elif score >= 75:
#     print('grade = 3.5')
# elif score >= 70:
#     print('grade = 3')
# elif score >= 65:
#     print('grade = 2.5')
# elif score >= 60:
#     print('grade = 2')
# elif score >= 55:
#     print('grade = 1.5')
# elif score >= 50:
#     print('grade = 1')
# else:
#     print('grade = 0')


score1 = input('กรุณาใส่คะแนนครั้งที่ 1 :')

if score1 == 'W':
    print('ติด ร')
else:

    score1 = int(score1)
    if score1 <= 30:
        print('ok')
    else : 
        print('ใส่คะแนนอีกครั้ง')

    score2 = int(input('กรุณาใส่คะแนนครั้งที่ 2 :'))
    if score2 <= 20:
        print('ok')
    else : 
        print('ใส่คะแนนอีกครั้ง')

    score3 = int(input('กรุณาใส่คะแนนครั้งที่ 3 :'))
    if score3 <= 30:
        print('ok')
    else : 
        print('ใส่คะแนนอีกครั้ง')

    score4 = int(input('กรุณาใส่คะแนน Final :'))
    if score4 <= 20:
        print('ok')
    else : 
        print('ใส่คะแนนอีกครั้ง')

    total_score = score1 + score2 + score3 + score4
    if total_score >= 80:
        print('grade = 4')
    elif total_score >= 75:
        print('grade = 3.5')
    elif total_score >= 70:
        print('grade = 3')
    elif total_score >= 65:
        print('grade = 2.5')
    elif total_score >= 60:
        print('grade = 2')
    elif total_score >= 55:
        print('grade = 1.5')
    elif total_score >= 50:
        print('grade = 1')
    else:
        print('grade = 0')


