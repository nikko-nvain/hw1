print("Второе задание, первый пункт")
a = int(input())
if a >= 0:
    print(a+1)
elif a < 0:
    print(a-2)

print("Второе задание, второй пункт")
first = int(input())
second = int(input())
third = int(input())

max_numb = first
if second > max_numb:
    max_numb = second
if third > max_numb:
    max_numb = third

min_numb = first
if second < min_numb:
    min_numb = second
if third < min_numb:
    min_numb = third

print(min_numb, max_numb)