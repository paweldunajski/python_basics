def max_num(num1, num2, num3):
    if num1 == num2 or num2 == num3 or num3== num1:
        print("takie same liczby")
    elif num1 >= num2 and num1>= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(300, 400, 67))


a = [300, 600, 67]
a.sort()
print(a[-1])