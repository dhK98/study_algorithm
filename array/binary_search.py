def binary_search(array, search_value):
     lower_bound = 0
     upper_bound = array.length - 1

     while lower_bound <= upper_bound:
          mid_point = (upper_bound + lower_bound) / 2
          mid_value = array[mid_point]

          if search_value == mid_value:
               return mid_point
          elif search_value < mid_value:
               upper_bound = mid_point - 1
          elif search_value > mid_value:
               lower_bound = mid_point + 1

     return 0