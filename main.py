def listMultiple(arr1,arr2):
  firstSet = set(arr1)
  secondSet = set(arr2)

  

  if firstSet.intersection(secondSet):
     return True
  else:
    return False
  
# note this method wil only work depending on the inputs being passed IE since we are using set operations only immutable data types can be utilized (NO dictonaries or lists as elements of arr1 or arr2)
print(listMultiple(['a','b','f','d','s','e','l'],['b''e','w','p','a']))

print(listMultiple([1,2,3,4,],[1,2,3,45,5,43,3,45]))

print(listMultiple(["a"],[""]))