import itertools


comb = itertools.product(["Л","О","Н"],repeat=4)
a = 0
for i in comb:
    a += 5
 #   i = list(i)
  #  for j in range (5):
   #     i.insert(j,"С")
    #    a += 1
     #   print(i)
      #  i.remove ("С")
print(a)