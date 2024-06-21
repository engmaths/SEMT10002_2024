#---------------------------------------------------------------
# Start of function definitions
#---------------------------------------------------------------

def find_min(L):
    """
    This function finds the minimum value in a list of numbers
    and its index.

    Inputs:
    L = a list of numbers

    Outputs:
    ind_min = the index of the minimum value
    min_val = the minimum value
    """

    # Assume the first element is the minimum to get things started
    ind_min = 0
    min_val = L[ind_min]

    # Now loop through all of the elements in the list L
    # and compare with the current minimum stored in min_val
    for i in range(len(L)):

        # If the current element is smaller than the current minumum
        # then update min_val and its index ind_min
        if L[i] < min_val:
            ind_min = i
            min_val = L[i]

    # return the index and value of the minimum
    return ind_min, min_val


def swap_values(ind_1, ind_2, L):
    """
    This function swaps the values of two elements that
    are stored in a list.

    Inputs:
    ind_1, ind_2 = the indices of the elements that will
    be swapped

    Outputs:
    L = the updated list
    """

    # define a temporary variable to store the value at
    # index ind_1
    tmp = L[ind_1]

    # update the element with index ind_1 with value of the element
    # at ind_2
    L[ind_1] = L[ind_2]

    # use the temp variable to update the value of the element with index
    # ind_2
    L[ind_2] = tmp
    
    return L


def my_sort(L):
    """
    This function sorts a list of numbers. We first find the min value
    of the whole list and swap it with the first element in the list.
    Then we look for the minimum in a sub-list that contains the
    all of the elements of the original list except the first. We swap
    the min with the second element in the original list. 
    We then repeat the process using smaller and smaller sublists,
    swapping the third, fourth, etc elements in the original list.

    Inputs:
    L = the list of numbers to be sorted

    Outputs:
    L = the sorted list
    """

    # Use a loop to create smaller and smaller sub-lists and
    # find the min of these sub-lists
    for i in range(len(L)):

        # create the sublist
        sublist = L[i:]

        # find min value in the sub-list
        ind_min_sub, min_val_sub = find_min(sublist)

        # convert the index of the sub-list into the index
        # of the original list
        ind_min = i + ind_min_sub

        # now use the indices to swap values
        L = swap_values(i, ind_min, L)

    return L



#---------------------------------------------------------------
# End of function definitions
#---------------------------------------------------------------

# define the list to be sorted
L = [6, 3, 7, -3, 1, 5, 2]

# print the original list and the sorted list
print('The original list is', L)
print('The sorted list is  ', my_sort(L))
