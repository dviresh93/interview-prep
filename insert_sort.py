def insert_sort(arr): 
    for i in list(range(len(arr))):
        current_val=arr[i] 
        index = i-1
        while(index>=0 and (arr[index]>current_val)):
            arr[index+1] = arr[index]
            index=index-1
        arr[index+1] = current_val
    return arr 

# print(insert_sort([1,2,9,4,7,6,5,8,3]))
# print(insert_sort([1,2,9,4,3]))
print(insert_sort([8,2,9,4,7,6,5,1,3]))

# took me more than 30-minutes, did not time myself after that 
# I was not able to translate logic to code 
# i had trouble/confusion on translating pseudo code to code 

# NEXT TIME: 
# - learn to write pseudo code on own 
# - then be able to translate psuedo code to actual code 
