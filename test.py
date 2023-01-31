import math
num1 = math.sqrt(49)
num2 = math.sqrt(9)
sum = (num1 + num2) * 10

str1 = "amazon"
str2 = "wert von {2}€".format(num1, num2, sum)

print(str1 + str2)