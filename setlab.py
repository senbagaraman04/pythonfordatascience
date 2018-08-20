#Author Senbagaraman
#Sets excercise
print ("****************************")
print ("Sets Excercise")

set1 = {1,2}
set2 = set(set1)

print (set2)

print ("Adding new data to the set")

set2.add("Test3")

print ("#set2.Add(Test3)\nset1")
print (set2)

print("Removing te data from the set")

set2.remove(2)

print (set2)


print("Chec something whther present or not")

x = "2" in set2

print x

print ("union of two sets")

set3 = set1 & set2
print (set3)

print ("Union of two sets")
print (set1.union(set3))


music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul", \
                    "progressive rock", "soft rock", "R&B", "disco"])
print (music_genres)

print ("convert the list to set")
set2 = ['rap','house','electronic music', 'rap']

set3 = set(set2)

print (set3)

print ("Let us get the sum of the claimed sales:Consider the list A=[1,2,2,1] and set B=set([1,2,2,1]), does sum(A)=sum(B)")

A = [1,2,2,1]
B = [1,2,2,1]
a = set(A)
b = set(B)

print (sum(a)==sum(b)) 
