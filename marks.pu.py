'''
#marks >50 average >60 good >90 excellent
marks=float(input("Enter marks:"))
if marks>50 and marks<=60:
    print("Average")
elif marks>60 and marks<=90:
    print("good")
elif marks>90:
    print("Excellent")
elif marks>=50:
    print("below Average")
else:
    print("invalid")
'''
'''
#1-5km perkm 5 6-12 perkm 6 13-20 perkm 8 21-30km 10 ola bill:6
km=float(input("Enter no of kms :"))
if km>1 and km<=5:
    print(km*5)
elif km>=6 and km<=12:
    print((km-5)*6+25)
elif km>=13 and km<=20:
    print((km-12)*8+25+42)
elif km>=20 and km<=30:
    print((km-20)*10+25+42+64)
elif km>30:
    print("ride not possible")
else:
    print("not valid km")
 '''

#

