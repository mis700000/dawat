from collections import Counter 
m1=["orange","apple","watermelon","orange","watermelon"]
print Counter(m1)

m1.sort()
print m1
for i in range(5):
   print i,"value of loop :",m1[i]
   
   
d1={"faheem":"pakistan","irfan":"india","muslim":"Jannah"}
for user,country in d1.iteritems():
    print user ,"belongs to",country 
