num1 = [2,6,4]
num2 = [9,7,5]
num1.sort()
num2.sort()
if num1==num2:
    print("0")
else:
    for i in range(len(num1)):
        print(num2[i]-num1[i])
