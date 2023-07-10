for text in range(3):
    print("hello",(text+1),(text + 1 )* "*" )

for text in range(2,10,2):
    print("hello",text,(text + 10 )* "*" )

suc = True
for text in range(3):
    print("Attempt")
    if suc :
        print("Suc")
        break
else :
    print("Attempted 3 times failed")

for x in range (5):
    for y in range(3):
        print(x,y)