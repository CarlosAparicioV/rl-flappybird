import json
import heapq

try:
    fil = open("rl-flappybird\data\qvaluesFinal.json", "r")
except IOError:
    print("error")
file = json.load(fil)

print(file["0_0_0_0"])

# maxValue = 0
# state = "0_0_0_0"
# for key,values in file.items():
#     #print(key)
#     #print(values[2])
    
#     if values[2]>maxValue:
#         maxValue = values[2]
#         state = key
        
        
# print(state)
# print(maxValue)



state2 = max(file, key=lambda key:file[key][-1])
maxValue2 = file[state2][-1]
        
print(state2)
print(maxValue2)


k = 20  # Number of keys to find

# Use heapq.nlargest with a custom key function
keys_with_largest_values = heapq.nlargest(k, file, key=lambda key: file[key][-1])
largest_values = [file[key][-1] for key in keys_with_largest_values]

print("Keys with largest values:", keys_with_largest_values)
print("Largest values:", largest_values)