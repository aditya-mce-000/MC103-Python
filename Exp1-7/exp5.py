colors = {"Red", "Blue", "Green"} 
print("Original Set =", colors) 
colors.add("Yellow") 
print("After Insert =", colors) 
colors.remove("Blue") 
print("After Delete =", colors)

numbers = (10, 20, 30, 40) 
print("Original Tuple =", numbers) 
new_tuple = numbers + (50,) 
print("After Insert =", new_tuple) 
new_tuple = new_tuple[:2] + new_tuple[3:] 
print("After Delete =", new_tuple)