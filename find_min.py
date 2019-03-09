numbers = [34, 432, 1, 99]

champion = 440 #すべての要素の値より小さい必要がある

for number in numbers:
    if number < champion:
        champion = number

print(champion)