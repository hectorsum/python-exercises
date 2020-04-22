#Retornar el mayor,medio y menor


##### Easiest way
nums = [int(input(f'Num {i+1}: ')) for i in range(3)] 
sorted(nums) #Sort numbers

##### Output            
print(f'Greatest number: {nums[0]}')
print(f'Middle number: {nums[1]}')
print(f'Lowest number: {nums[2]}')





#### Antoher option
greatest = nums[0]
lowest = nums[0]
middle = nums[0]

for i in range(len(nums)): #Bubble sort
    for x in range(len(nums)-1):
        if nums[x] > nums[x+1]:
            aux = nums[x+1]
            nums[x+1] = nums[x]
            nums[x] = aux            
##### Output
print(f'Greatest number: {nums[2]}') #last value is the greatest according when using bubble sort method
print(f'Middle number: {nums[1]}') 
print(f'Lowest number: {nums[0]}')
