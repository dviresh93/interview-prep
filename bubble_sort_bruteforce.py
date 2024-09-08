def bubble_sort(arr): 
    for i in list(range(0, len(arr)-1)): 
        for j in list(range(len(arr)-1, i, -1)): # this will ensure the list is in descending order
            if arr[j-1] > arr[j]: 
                tmp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = tmp   
    return arr 

print(bubble_sort([1, 2, 3, 4, 5]))
print(bubble_sort([3, 1, 2, 4, 5]))
print(bubble_sort([3, 5, 2, 4, 1]))
print(bubble_sort([4, 5, 3]))
print(bubble_sort([3]))

# this was timed and took me an hour to solve 
# reason for getting stuck: 
# my "range" was wrong, i was doing range(0, 5) - this was not expanding to a list, not sure why 
# so I had to do lis(rage(3,5)), just and example, this ate lot of my time 
# onec this was done, my inner loop was running wrong, the way i identified thisn was to print "j"
# i saw that the inner loop end point was not correct, I had (range(len(arr)-1, i+1 , -1))instrad of whats currently implemented,
# i got cofused by looking at pseudo code from the class
