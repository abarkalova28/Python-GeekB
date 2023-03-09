num = int(input("Введите трехзначное число: "))

hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10

sum = hundreds + tens + ones

print ("Сумма цифр числа", num,"равна", sum)
