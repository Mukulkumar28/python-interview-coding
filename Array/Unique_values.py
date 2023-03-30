#   set is a fucntion which not take the duplicate values

n = int(input("Enter the total numbers you want to print :"))
l = []
for i in range(n):
   ele = input("enter the element")
   l.append(ele)
print("my list",l)
unique_value = set(l)
print(unique_value)
  
  
  