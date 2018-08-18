#tuples lab assignments
print ("\n\nAuthor: Senbagaraman")
print ("Lines printed with # are actual coding line, which will provide the desired result beneath it")
print ("*************************************") 

tuple1=("test",4,2)
tuple1
print ("Printing the tuple")
print tuple1
print ("\n\n#print type(tuple1)")
print type(tuple1)

print ("\n\nNow Printing the second element in te above tuple")
print ("#print tuple[1]")
print tuple1[1]

print ("\n\n We can also print the type of each value in the tuple")
print ("#print type(tuple1[1])")
print type(tuple1[1])

print ("\n\nWe can add some data to the tuple by concatenating them")
print ("#tuple2 = tuple1 + ( 5,6,4)")
tuple2 = tuple1 + ( 5,6,4)
print ("#print tuple2")
print tuple2

print ("\n\nTo find the index of some value in tuple")
print ("#print tuple1.index(5)")
print tuple1.index(4)

print ("\n\nmake the tuple as sorted")
print ("#print (sorted(tuple1))")
print (sorted(tuple1))
