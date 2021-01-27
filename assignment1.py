# Use python lists and make an list of numbers.
# Write a function which returns sum of the list of numbers

def calculate_sum(elements,n):
  sum=0
  for i in range(0,n):
    sum=sum+elements[i]
  return sum
elements=[]
n = int(input("Enter number of elements : "))
print("Enter the elements")
for i in range(0,n):
  ele=int(input())
  elements.append(ele)
value = calculate_sum(elements,n)
print("The Total Sum is",value)