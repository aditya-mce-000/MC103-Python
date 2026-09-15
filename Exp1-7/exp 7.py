def search_list(values, key):    
    for i in range(len(values)):        
        if values[i] == key:            
            return i    
    return -1 
numbers = [12, 25, 7, 40, 18, 30] 
key = 18 
position = search_list(numbers, key) 
print("List =", numbers) 
print("Number to search =", key) 
if position != -1:    
    print("Number found at index", position) 
else:    
    print("Number not found")