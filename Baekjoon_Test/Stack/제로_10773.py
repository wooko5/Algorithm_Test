stack = []
for _ in range(int(input())):
    number = int(input())
    if number == 0 and stack:
        stack.pop()
    else:
        stack.append(number)
print(sum(stack))