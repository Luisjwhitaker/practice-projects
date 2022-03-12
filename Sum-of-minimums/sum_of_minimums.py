def sum_of_minimums(numbers):
    minimum_values=[0]
    for array in numbers: # iterating through each list within the "master" list
        current_minimum = array[0] # set the current minimum as the first number in the list
        for number in array: # itterating through each number in the list
            if number < current_minimum:
                current_minimum = number # if the current number is smaller then our curent smallest number (current_minimum), make it our new smallest number (current_minimum)
        minimum_values.append(current_minimum) # save the smallest number in the current list (current_minimum) to the "master" list of all our smallest numbers (minimum_values)

    return sum(minimum_values) # add up all the smallest numbers from each list and return the sum

print(sum_of_minimums([[2,7,5],[2,0]])) # Example test, should return 2.
                                        # thats because the lowest number for the first list is 2 and the lowest number in the second list is 0.
                                        # 2 + 0 = 2
