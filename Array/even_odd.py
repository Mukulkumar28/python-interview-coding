n = int(input("Enter total number: "))
arr = []
even = []
odd = []
for i in range(n):
    ele = int(input("Enter a number: "))
    arr.append(ele)
print("My list", arr)

for i in arr:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
        
print("even", even)
print("odd", odd)
