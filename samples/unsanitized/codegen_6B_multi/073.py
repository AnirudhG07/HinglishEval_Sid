
def smallest_change(arr):
    """
    Ek array arr diya gaya hai integers ka, usme se minimum kitne elements ko change karna padega 
    taaki array palindromic ban jaye. Ek palindromic array woh hota hai jo aage se bhi aur peeche se bhi 
    same padhta hai. Ek change me, aap ek element ko kisi bhi dusre element se replace kar sakte ho.

    Jaise ki:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    smallest_list = []
    max_element = -1
    for item in arr:
        temp_arr = sorted(list(reversed(arr)))
        new_arr = temp_arr[0] + temp_arr[1]
        if len(min(new_arr, item)) <= len(max_element):
            max_element = item
            smallest_list = [new_arr, list(reversed(new_arr))]
        temp_arr = temp_arr[0:]
    return smallest_list

smallest_change([1,2,3,5,4,7,9,6])
smallest_change([1, 2, 3, 4, 3, 2, 2])
smallest_change([1, 2, 3, 2, 1])
