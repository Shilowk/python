#selection sort
input("Press Enter to work through this code step-by-step")

#here is the list we are going to sort
my_list = [85, 24, 63, 45, 17, 31, 96, 50]

#we are going to use a for loop to go through the list one index (position) at a time
for index in range(len(my_list) - 1):
    #print the list
    print("The list is currently: ")
    print(my_list)
    input()
    #we are going to look at everything after the index we are on, and we will get the minimum
    print("We are going to swap " + str(my_list[index]) + " with the smallest value in the list after this point, but only if the smallest value is less than " + str(my_list[index]) + ". The values after " + str(my_list[index]) + " are:")
    #the list starts at element (index+1) and the colon (:) means that we go on until the end of the list
    print(my_list[index+1:])
    input()
    
    next_min_value = min(my_list[index + 1:])
    input("The minimum value from here is: " + str(next_min_value))
    
    if next_min_value < my_list[index]:
        input(str(next_min_value) + " is less than " + str(my_list[index]) + ", so we will swap their positions in the list.")
        next_min_index = my_list.index(next_min_value)
        input(str(next_min_value) + " is in list position " + str(next_min_index))
        input(str(my_list[index]) + " is in list position " + str(index))
        input("We will now swap their postions")
        
        #we move the value we are at in the loop to the position of the minimum
        my_list[next_min_index] = my_list[index]
        #we move the minimum to the position of the number we are at in the loop
        my_list[index] = next_min_value
    else:
        input(str(next_min_value) + " is greater than " + str(my_list[index]) + ", so " + str(my_list[index]) + " is in the right place.")
print("We are now finished. The fully sorted list is:")
print(my_list)  