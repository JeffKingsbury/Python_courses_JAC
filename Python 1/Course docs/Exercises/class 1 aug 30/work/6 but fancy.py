dollar = int(input("Please enter a dollar amount: "))

print("Breakdown:")
for label, div in {'five dollar bills' : 5, 'toonies' : 2 , 'loonies' : 1}.items():
    num = int(dollar / div)
    if num > 0:
        print('{} {}'.format(num, label if num > 1 else label[:-1]))
        dollar = dollar - (num * div)