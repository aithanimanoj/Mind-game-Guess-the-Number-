gn=int(input("Enter a Number(inbetween 1 to 100):"))
if gn<0 or gn>100:
    Print("Enter a number within range!!!!!!!!!!!!")
ln=0
un=100
while True:
    m=int((ln+un)/2)
    print("guessed number is {} is it correct if Y/N".format(m))
    if(input=='Y' or input()=='y'):
        break;
    if gn>m:
        ln=m
        un=un
    elif gn<m:
        ln=ln
        un=m
