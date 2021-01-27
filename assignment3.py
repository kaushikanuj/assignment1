def getMaxLength(arr, n): 
  
    count = 0 
    result = 0 
  
    for i in range(0, n): 
      
        if (arr[i] == 0): 
            count = 0
  
        else: 
              
            count+= 1 
            result = max(result, count)  
          
    return result  
elements=[]
n = int(input("Enter number of elements : "))
print("Enter the elements")
for i in range(0,n):
  ele=int(input())
  elements.append(ele) 
n = len(elements)

print("The Maximum number of 1's are",getMaxLength(elements, n))
