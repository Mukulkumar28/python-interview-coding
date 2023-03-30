
# maximum, minimum and second largest number in array
n = int(input("enter total number of values: "))
arr=[]

for i in range(n):
    ele=int(input("Enter the number"))
    arr.append(ele)
print("my list",arr)

sorted_values = arr.sort()
print("sorted values", arr)

minimum = arr[0]
print(minimum)

maximum = arr[-1]
print(maximum)

sec_largest = arr[-2]
print(sec_largest)