numbers = [34, 432, 1, 99]

#numbersの合計値をforを使って出力してください

total = 0

for number in numbers:
    total = total + number

print(total)


total = 0

for number in numbers:
    total += number

print(total)

