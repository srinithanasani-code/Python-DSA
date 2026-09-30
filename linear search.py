def linearsearch(a,el):
  ar=[]
  for i in range(len(a)):
    if a[i]==el:
      # print(f'{el} if found at index {i}')
      ar.append(i)
  # print('element not found')
  if len(ar)>0:
    return ar
  return -1
a=[12,3,14,22,56,75,14]
print(linearsearch(a,15))