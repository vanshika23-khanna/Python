#Q76. Armstrong number

def is_armstrong(num):
    temp=num
    sum_of_powers=0
    num_digits=len(str(num))
    while(temp>0):
        digit=temp%10
        sum_of_powers+=digit**num_digits
        temp=temp//10
    return sum_of_powers==sum_of_powers
a=int(input("Enter the upper range for Armstrong numbers: "))
for i in range(1,a+1):
    if is_armstrong(i):
        print(i)
print("\n\nThis program is executed by Vanshika Khanna , 0231BCA033")
