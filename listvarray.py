list_two=list(range(1,4))
list_three = list(range(1,4))
list_sum = []

for index in range(3):
    list_two(index) = list_two(index) ** 2
    list_three(index) = list_three(index) ** 3
    list_sum.append(list_two(index)+list_three(index))

print(list_sum)
print(list_two)
