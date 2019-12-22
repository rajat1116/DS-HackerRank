# Simple code Sparse Array 

def matchingStrings(arr, q):
  count = 0
  res = []
  for i in range(len(q)):
    for j in range(len(arr)):
      if q[i] == arr[j]:
        count += 1
    res.append(count)
    count = 0
  return res 
  
