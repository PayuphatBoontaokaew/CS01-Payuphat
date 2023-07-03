score1 = float(input('กรุณาใส่คะแนนเก็บของคุณ :'))
if score1 <= 30  :
    print('ok')
else :
    print('Error')
score2 = float(input('กรุณาใส่คะแนนกลางภาคของคุณ :'))
if score2 <= 30  :
    print('ok')
else :
    print('Error') 
score3 = float(input('กรุณาใส่คะแนนปลายภาคของคุณ :'))
if score3 <= 40  :
    print('ok')
else :
    print('Error')

score = score1 + score2 + score3

if score >= 80 :
    print('grade = A')
elif score >=  75 :
    print('grade = B+')
elif score >=  70 :
    print('grade = B')
elif score >=  65 :
    print('grade = C +')
elif score >=  60 :
    print('grade = C')
elif score >=  55 :
    print('grade = D +')
elif score >=  50 :
    print( 'grade = D' )
else :
    print('grade = F')

