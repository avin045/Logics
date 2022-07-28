arr = [3,2,5,6,1];
#      0 1 2 3 4 
len_arr = len(arr); # 6


# Traverse
for i in range(len_arr):
  for j in range(i+1,len_arr):
    if arr[i] > arr[j]:
      arr[i],arr[j] = arr[j],arr[i]
print(arr)

# OUTPUT:
# [1,2,3,5,6]
# --------------------------------- #
'''
1. compare
2. if arr[0] > arr[1]
      arr[0],arr[1] = arr[1],arr[0]
      47      1          1    47

      i = 0  :  j = 1
      47 = 1
      47 = 10
      47 = 25
      47 = 19
      47 = 2

'''
# --------------------------------- #
