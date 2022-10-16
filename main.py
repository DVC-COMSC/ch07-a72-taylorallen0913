
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

is_sublist = True

for num in num2:
    if num in num1:
        # Remove from major list so no duplicate problem
        num1.remove(num)
    else:
        is_sublist = False

print(is_sublist)
